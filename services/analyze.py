import json
import os
import random
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from services.External_AI_Models import extract as extract
from services import navigation as navigation
from services.External_AI_Models import gemeni as gemeni
from services.APIs import gecko as gecko
from services.Data.markdowns import MkPriceOp as prcmarkdown
from services.Scrapers import bonbast as bonbast
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
QueuePath = os.path.join(project_root, 'services', 'Data', 'analyze')
InputPath = os.path.join(project_root, 'Local_AI_Models', 'InputData')



class Analyze():
    def __init__(self):
        self.gemeni_inprocess = False
        self.localai_inprocess = False
        self.gemeni_active = True
        self.localai_active = True
        self.status = []
        self.lastStatus = self.LastsStatus()
        self.status = self.lastStatus["Status"]
        
        
    def manage(self):
        for item in self.status:
            itemId = self.status.index(item)
            if item["status"] == "in Queue":
                data = self.loadQueue()["Data"][itemId]
                if data:
                    if self.gemeni_active:
                        while self.gemeni_inprocess:
                            print("External Ai is buissy, wating for 10 seconds")
                            time.sleep(10)
                        item["status"] = "pending"
                        item["external model"] = "pending"
                        tryExternal = self.geminiAnalyze(data)
                        print(f" try external = {tryExternal}")
                        if tryExternal:
                            item["status"] = "done"
                            item["external model"] = "verified"
                            self.saveStatus(self.status)
                        else:
                            item["status"] = "failed"
                            item["external model"] = "failed"
                            self.saveStatus(self.status)
                            if self.localai_active:
                                item["local model"] = "pending"
                                self.saveStatus(self.status)
                                self.addtoLocal(data)
                            else:
                                print("local AI was not active")
                                
                    elif self.localai_active:
                        item["local model"] = "pending"
                        self.saveStatus(self.status)
                        self.addtoLocal(data)
                    else:
                        print("Nither local Ai or External Ai Are Active")
                                
                                





    def loadQueue(self):
        try:
            with open(os.path.join(QueuePath, "Queue.json"), 'r', encoding='utf-8') as file:
                last_data = json.load(file)
                return last_data
        except Exception as e:
            print(
                f"there is an Error with Queue.json; {e}")
            
            
    def sendtoQueue(self, data):
        try:
                last_data = self.loadQueue()
                self.status.append({
                    "id": len(self.status),
                    "status": "in Queue",
                    "deployed date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                    "external model": "undefined",
                    "local model": "undefined"
                    
                })
                self.saveStatus(self.status)

        except Exception as e:
            print(
                f"Nav :there is an Error with Queue.json; {e}")
            return
        last_data["Data"].append(data)
        with open(os.path.join(QueuePath, "Queue.json"), 'w', encoding='utf-8') as file:
            json.dump(last_data, file, indent=4, ensure_ascii=False)
        self.manage()
        print("Queue.json has been updated; 1 Item added")



    def LastsStatus(self):
        try:
            with open(os.path.join(QueuePath, "Status.json"), 'r', encoding='utf-8') as file:
                last_status = json.load(file)
                return last_status
        except Exception as e:
            print(
                f"Nav :there is an Error with Status.json; {e}")
        
    def saveStatus(self, data):
        try:
            last_data = self.LastsStatus()
            last_data["Status"] = data
            with open(os.path.join(QueuePath, "Status.json"), 'w', encoding='utf-8') as file:
                json.dump(last_data, file, indent=4, ensure_ascii=False)
            print("Status saved")
        except Exception as e:
            print(f"there was an error while saving the Status.json : {e}")



    def addtoLocal(self, data, name="news"):
        print("going for local ")
        try:
            with open(os.path.join(InputPath, f"{name}.json"), 'r', encoding='utf-8') as file:
                last_data = json.load(file)
        except:
            print(f"{name}.json is not where it sould be at {InputPath}")
    
        last_data["Data"].append(data)
        
        with open(os.path.join(InputPath, f"{name}.json"), 'w', encoding='utf-8') as file:
                    json.dump(last_data, file, indent=4, ensure_ascii=False)
        print("data has been sent to Local AI")


    def geminiAnalyze(self, data):
            self.gemeni_inprocess = True
            try:
                print("data has been sent to External AI")
                self.result = gemeni.analyze(data)
                if self.result != None:
                    extract.ex.geminiMx1(self.result)
            except Exception as e:
                print(f"analyze failed canceled saving: {e}")
                self.gemeni_inprocess = False
                return False
            self.gemeni_inprocess = False
            return True

            

    def priceAnalyze(self):
        data = []
        geckoData = gecko.read("FullTimeCrypto")["CryptoData"]
        bonbastData = bonbast.load("FullTimeCurrency.json")["PriceData"]

        cryptoLast = geckoData[-1]
        bonbastLast = geckoData[-1]

        cryptoLastTime = datetime.strptime(
            geckoData[-1]["time"], "%Y-%m-%d %H:%M:%S")
        bonbastLastTime = datetime.strptime(
            geckoData[-1]["time"], "%Y-%m-%d %H:%M:%S")
        target_duration = timedelta(weeks=1)

        cryptoPast = min(
            geckoData[:-1],
            key=lambda item: abs(
                (cryptoLastTime -
                 datetime.strptime(item["time"], "%Y-%m-%d %H:%M:%S"))
                - target_duration
            ),
        )
        bonbastPast = min(
            bonbastData[:-1],
            key=lambda item: abs(
                (bonbastLastTime -
                 datetime.strptime(item["time"], "%Y-%m-%d %H:%M:%S"))
                - target_duration
            ),
        )

        data.append(cryptoPast)
        data.append(bonbastPast)
        data.append(cryptoLast)
        data.append(bonbastLast)

        GeminiResponse = gemeni.priceDetermine(data)
        if GeminiResponse and GeminiResponse.candidates:
            try:
                date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                mdText = GeminiResponse.text
                prcmarkdown.priceOp(mdText, date)
                navigation.nav.saveOpinion("PriceOp", date, mdText)
            except Exception as e:
                print(f"Failed to extract and save opinion: {e}")


az = Analyze()