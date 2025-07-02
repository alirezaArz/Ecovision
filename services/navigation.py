import json
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
Navpath = os.path.join(project_root, 'services', 'SnailData')


class Nav():
    def __init__(self):
        pass

    def Navread(self, name):
        try:
            with open(os.path.join(Navpath, f"{name}.json"), 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                return (self.data)
        except:
            print(
                f"Nav : {name}.json is not where it sould be at {Navpath}")

    def saveNavigation(self, data, adress):
        self.lastdata = self.Navread(adress)

    # - THIS IS WHERE WE SHOULD DELETE THE UNUSED NEWS ONLY IF THEY ARE OLDER THAN (for example 3days)
    # - AND WE START WITH 'LESS IMPORTANST' AND WILL CONTINU UNTILL THERE ARE 2 NEWS IN THE FILE
    # - SO THE FILE SHOULDNT BE EMPTY AT ALL!!!

        self.lastdata["newsData"].append(data)
        with open(os.path.join(Navpath, f"{adress}.json"), 'w', encoding='utf-8') as file:
            json.dump(self.lastdata, file, indent=4, ensure_ascii=False)

    def separate(self):
        print("navigating data")
        self.last_analyze = self.Navread('LastAnalyze')
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

nav = Nav()
#nav.separate()
