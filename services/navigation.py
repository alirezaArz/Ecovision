import json
import datetime
from datetime import timedelta
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
Navpath = os.path.join(project_root, 'services', 'Data', 'Navigations')
OpPath = os.path.join(project_root,'services','Data' ,'markdowns')


class Nav():
    def __init__(self):
        pass

    def Navread(self, name):
        try:
            with open(os.path.join(Navpath, f"{name}.json"), 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                return self.data
        except:
            print(
                f"Nav : {name}.json is not where it sould be at {Navpath}")

    def saveNavigation(self, data, adress):
        try:
            if adress != "PriceOpinion":
                self.lastdata = self.Navread(adress)
                self.lastdata["newsData"].append(data)
            else:
                self.lastdata = data
                
            with open(os.path.join(Navpath, f"{adress}.json"), 'w', encoding='utf-8') as file:
                json.dump(self.lastdata, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Nav: an error on saveNavigation : {e}")

    def deleteCycle(self):

        timenow = datetime.datetime.now()
        self.tobedeleted = []
        for newsdic in self.lastdata["newsData"]:
            a = datetime.datetime.fromisoformat(newsdic["date"])
            if timenow - a > timedelta(days=3):
                self.tobedeleted.append(newsdic)

        for cy in ["low", "medium", "high"]:
            for willdelete in self.tobedeleted:
                if willdelete["importance"] == cy:
                    if len(self.lastdata["newsData"]) > 2:
                        if willdelete in self.lastdata["newsData"]:
                            self.lastdata["newsData"].remove(willdelete)

    def separate(self):
        print("navigating data")
        #----------------------------------------------------------------

        lastlist = self.Navread("LastAnalyze")["newsData"]
        seen_titles = []
        clean_list = []

        for news in lastlist:
            title = news["title"]
            if title not in seen_titles:
                seen_titles.append(title)
                clean_list.append(news)

        self.last_analyze = {"newsData":clean_list}  
        #----------------------------------------------------------
        
        for item in self.last_analyze["newsData"]:
            if item["category"] == "Economy":
                self.saveNavigation(item, 'SnEconomy')

            elif item["category"] == "Finance":
                self.saveNavigation(item, 'SnFinance')

            elif item["category"] == "Markets":
                self.saveNavigation(item, 'SnMarkets')

            elif item["category"] == "Investing":
                self.saveNavigation(item, 'SnInvesting')

            elif item["category"] == "Technology":
                self.saveNavigation(item, 'SnTecnology')

            elif item["category"] == "Science":
                self.saveNavigation(item, 'SnScience')
        print("nav: data separated successfully!")
        self.output()
        self.outsite()

    def output(self):
        self.importance = "high"
        self.apnd_count = 0
        self.records = {'SnEconomy': 0, 'SnFinance': 0, 'SnMarkets': 0,
                        'SnInvesting': 0, 'SnTecnology': 0, 'SnScience': 0}
        self.lastOutPut = self.Navread("SnOutput")
        self.newOutPut = []
        self.mining()

        if self.apnd_count < 25:  # now we can set the budgets
            self.importance = "medium"
            self.mining()
            if self.apnd_count < 30:
                self.importance = "low"
                self.mining()

        all_used = False
        record_count = 0
        for item in self.records:
            if self.records[item] < 2:
                self.importance = "medium"
                self.mining(item)
                if self.records[item] < 2:
                    self.importance = "medium"
                    self.mining(item)

        self.lastOutPut["newsData"][:] = self.newOutPut
        with open(os.path.join(Navpath, "SnOutput.json"), 'w', encoding='utf-8') as file:
            json.dump(self.lastOutPut, file, indent=4, ensure_ascii=False)
        print("output ready")

    def mining(self, category=''):
        if category == '':
            for item in ['SnEconomy', 'SnFinance', 'SnMarkets', 'SnInvesting', 'SnTecnology', 'SnScience']:
                adding_item = self.Navread(item)
                for state in adding_item["newsData"]:
                    if state["importance"] == self.importance:
                        state["id"] = self.apnd_count
                        self.newOutPut.append(state)
                        self.apnd_count += 1
                        self.records[item] += 1
        else:
            adding_item = self.Navread(category)
            for state in adding_item["newsData"]:
                if state["importance"] == self.importance:
                    state["id"] = self.apnd_count
                    self.newOutPut.append(state)
                    apnd_count += 1
                    self.records[category] += 1

    def outsite(self):
        data = self.Navread("SnOutput")
        new_data = data["newsData"][:31]
        data["newsData"][:] = new_data

        with open(os.path.join(Navpath, "SnOutsite.json"), 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("out site ready")
        
    def OpRead(self, id):
        # reading the items file for each opinions
        try:
            with open(os.path.join(OpPath,id, "items.json"), 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                return (self.data)
            
        except:
            print(
                f"Nav : items.json is not where it sould be at {OpPath}/{id}")

    def lastOP(self, id):
        lastOp = self.OpRead(id)["dates"][-1]
        return lastOp
        
        
    def saveOpinion(self, id, name, file):
        try:
            lastOP = self.OpRead(id)
            
            try:
                output_filename = f"{id}({name}).md"
                with open(os.path.join(OpPath,id, '.md', output_filename), "w", encoding="utf-8") as f:
                    f.write(file)
                print('.md file saved successfully, going for saving the date...')
                
                lastOP["dates"].append(f"{id}({name})")
                with open(os.path.join(OpPath,id, "items.json"), 'w', encoding='utf-8') as file:
                    json.dump(lastOP, file, indent=4, ensure_ascii=False)
                print(".md file's date saved successfully")

            except Exception as e:
                print(f"threre was an error while saving the .md file proccess: {e}")
            
        except Exception as e:
            print(f"no valid value in {OpPath}/{id}/items.json['dates']")
        
        
nav = Nav()
