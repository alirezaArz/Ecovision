import os
import time
import json
from datetime import datetime
from halo import Halo

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
InputPath = os.path.join(project_root, 'Local_AI_Models', 'InputData')
OutPutPath = os.path.join(project_root, 'Local_AI_Models', 'OutputData')
import Ollama as ollama
class Core():
    def __init__(self):
        self.spinner = Halo(text='', spinner={
            "interval": 100,
            "frames": [
                "◜",
                "◠",
                "◝",
                "◞",
                "◡",
                "◟"
            ]
        })
        self.active = True
        self.list = []
        self.saveList(self.list)
    
    def checkInput(self,name='news'):
        try:
            with open(os.path.join(InputPath, f"{name}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
                return (data)
        except:
            print(f"Nav : {name}.json is not where it sould be at {InputPath}")
        
    def clearInput(self, step=1, name='news'):
        last_data = self.checkInput()
        data_length = len(last_data["Data"])
        
        if data_length >= step:
            for i in range(step):
                del last_data["Data"][0]
            with open(os.path.join(InputPath, f"{name}.json"), 'w', encoding='utf-8') as file:
                    json.dump(last_data, file, indent=4, ensure_ascii=False)
        else:
            print(f"input data's length is {data_length} and less than clear step!,canceled deleting")
    
    
    
    def readOutput(self,name='news'):
        try:
            with open(os.path.join(OutPutPath, f"{name}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
                return (data)
        except:
            print(f"{name}.json is not where it sould be at {OutPutPath}")
    
    def saveOutput(self, data, Id, name='news'):
        
        print("insight: saving the result")
        last_data = self.readOutput()
        new_data = {
            "id":Id,
            "response": data
        }
        last_data["Data"].append(new_data)
        
        with open(os.path.join(OutPutPath, f"{name}.json"), 'w', encoding='utf-8') as file:
                    json.dump(last_data, file, indent=4, ensure_ascii=False)
    def saveList(self, lst, name='news'):
        last_data = self.readOutput()
        last_data["list"] = lst
        with open(os.path.join(OutPutPath, f"{name}.json"), 'w', encoding='utf-8') as file:
                    json.dump(last_data, file, indent=4, ensure_ascii=False)
            
    def server(self):
        self.firstloop = True
        #self.spinner.start()
        self.deniedloops = 0
        self.lastItemCount = 0
        
        while self.active:
            if self.firstloop:
                print("local Ai: running Local Analyzation Core...")
                print("local Ai: checking for input Data...")
                self.inputData = self.checkInput()["Data"]
                self.itemCount = len(self.inputData)
                if self.itemCount == 0:
                    print(f"local Ai: There are no items inside News.json")
                self.firstloop = False
            else:
                self.inputData = self.checkInput()["Data"]
                self.itemCount = len(self.inputData)
            
            if self.itemCount >= 1:
                if self.itemCount - self.lastItemCount > 0:
                    print(f"local Ai: {self.itemCount} new item(s) detected!")
                self.lastItemCount = self.itemCount
                self.deniedloops = 0
                analyzed_result = ollama.answer(self.inputData[0])
                input_dataId = self.inputData[0]["id"]
                self.list.append(input_dataId)
                self.saveList(self.list)
                if analyzed_result:
                    self.saveOutput(analyzed_result, input_dataId)
                    self.clearInput()
                    self.inputData = self.checkInput()["Data"]
                    self.itemCount = len(self.inputData)
                    if self.itemCount == 0:
                        print('local Ai: all datas have been analyzed successfully!')
                
                time.sleep(7)
                
            else:
                
                time.sleep(7)
                #self.deniedloops += 1
                if self.firstloop and self.deniedloops >= 12:
                    print(f"local Ai: {self.deniedloops} denied loops!... shuting down the server.")
                    self.active = False
                    
                    
        #self.spinner.stop()
    
 
insight = Core()
insight.server()
