import json
import os
import random
import time
import re
from services import systems as system
from datetime import datetime, timedelta, timezone
from services.External_AI_Models import extract as extract
from services import navigation as navigation
from services.External_AI_Models import gemini as gemini
from services.APIs import gecko as gecko
from services.Data.markdowns import MkPriceOp as prcmarkdown
from services.Scrapers import bonbast as bonbast
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
Navpath = os.path.join(project_root, 'services', 'Data', 'Navigations')
QueuePath = os.path.join(project_root, 'services', 'Data', 'analyze')
InputPath = os.path.join(project_root, 'services',
                         'Local_AI_Models', 'InputData')
OutPutPath = os.path.join(project_root, 'services',
                          'Local_AI_Models', 'OutputData')


class Analyze():
    def __init__(self):
        self.priceAnalyzeActive = False
        self.priceAnalyze_inprocess = False
        self.gemini_inprocess = False
        self.localai_inprocess = False
        self.gemini_active = False
        self.localai_active = False
        self.privateLoopWating = False
        self.snailActive = False
        self.waitingForLocal = False
        self.status = []
        self.lastStatus = self.LastsStatus()
        self.memoId = self.lastStatus["memoId"]
        self.localPending = self.lastStatus["localPending"]
        if self.localPending:
            self.waitingForLocal = True

            print("Snail: checking the local output")
        self.status = self.lastStatus["Status"]

    def manage(self, target="none"):
        if target != "none":
            print(
                f"analyze: manager has been started with AI target of {target}")
        else:
            print("analyze: manager has been started without any specific AI target")
        for item in self.status:
            itemId = item["id"]
            if item["status"] == "in Queue" or item["status"] == "failed":
                raw_list = self.loadQueue()["Data"]
                if raw_list:
                    for element in raw_list:
                        if element["id"] == itemId:
                            data = element
                        else:
                            print(
                                f"item with id of {item["id"]} doesn't have any property or data in queue.json")
                            data = None
                    if data:
                        if (self.gemini_active and target == "none") or target == "external":
                            while self.gemini_inprocess:
                                print(
                                    "External Ai is buissy, wating for 10 seconds")
                                time.sleep(10)
                            item["status"] = "pending"
                            item["external model"] = "pending"
                            tryExternal = self.geminiAnalyze(data)
                            if tryExternal:
                                item["status"] = "done"
                                item["external model"] = "verified"
                                self.clearQueue(element["id"])
                                self.saveStatus(self.status)
                            else:
                                item["status"] = "failed"
                                item["external model"] = "failed"
                                self.saveStatus(self.status)
                                if self.localai_active and target == "none":
                                    item["status"] = "pending"
                                    item["local model"] = "pending"
                                    self.localPending.append(item["id"])
                                    self.saveStatus(self.status)
                                    self.addtoLocal(data)

                                else:
                                    print("local AI was not active")

                        elif (self.localai_active and target == "none") or target == "local":
                            item["status"] = "pending"
                            item["local model"] = "pending"
                            if item["id"] not in self.localPending:
                                self.localPending.append(item["id"])
                            self.saveStatus(self.status)
                            self.addtoLocal(data)

                        else:
                            print("Nither local Ai or External Ai Are Active")
                else:
                    print("there are no item in Queue.json's Data list")

    def checkLocalOutput(self):
        last_data = self.readOutput()
        if last_data["Data"]:
            for item in last_data["Data"]:
                if item["id"] in self.localPending:
                    print(f"found an item with id of: {item["id"]}")
                    new_list = []
                    new_result = json.loads(item["response"])

                    for it in new_result:
                        if it != 'id':
                            new_list.append(new_result[it])
                    lastResult = system.vgsy.Navread("LastAnalyze")
                    lastResult["newsData"][:] = new_list
                    with open(os.path.join(Navpath, "LastAnalyze.json"), 'w', encoding='utf-8') as file:
                        json.dump(lastResult, file, indent=4,
                                  ensure_ascii=False)

                    navigation.nav.separate()
                    self.clearcache(item["id"])
                else:
                    print(
                        f"there is an item with id of {item["id"]} that doesnt have any parrent in status local pendings")
                    self.clearOutput(item["id"])

    def clearcache(self, id):
        for item in self.status:
            if item["id"] == id:
                # del self.status[self.status.index(item)]
                item["status"] = "done"
                item["local model"] = "verified"
                # del self.memoId[self.memoId.index(id)]
                del self.localPending[self.localPending.index(id)]
                self.saveStatus(self.status)
                print(f" item {id} has been removed from status.json")

        self.clearQueue(id)
        print(f" item {id} has been removed from Queue.json")

        # ------------------ this part has been commented out to test the output data of local analyze
        self.clearOutput(id)
        print(f" item {id} has been removed from outputData -> news.json")

        self.waitingForLocal = False
        self.privateLoopWating = False
        print("stopped searching for local output data")

    def readOutput(self, name='news'):
        try:
            with open(os.path.join(OutPutPath, f"{name}.json"), 'r', encoding='utf-8') as file:
                data = json.load(file)
                return (data)
        except:
            print(f"{name}.json is not where it sould be at {OutPutPath}")

    def clearOutput(self, id):
        last_data = self.readOutput()
        last_dataList = last_data["Data"]
        for item in last_dataList:
            if item["id"] == id:
                del last_dataList[last_dataList.index(item)]
        self.saveOutput(last_dataList)

    def saveOutput(self, data, name='news'):
        last_data = self.readOutput()
        last_data["Data"] = data

        with open(os.path.join(OutPutPath, f"{name}.json"), 'w', encoding='utf-8') as file:
            json.dump(last_data, file, indent=4, ensure_ascii=False)

    def loadQueue(self):
        try:
            with open(os.path.join(QueuePath, "Queue.json"), 'r', encoding='utf-8') as file:
                last_data = json.load(file)
                return last_data
        except Exception as e:
            print(
                f"there is an Error with Queue.json; {e}")

    def clearQueue(self, id):
        last_queue = self.loadQueue()
        last_queueList = last_queue["Data"]
        for item in last_queueList:
            if item["id"] == id:
                del last_queueList[last_queueList.index(item)]
        with open(os.path.join(QueuePath, "Queue.json"), 'w', encoding='utf-8') as file:
            json.dump(last_queue, file, indent=4, ensure_ascii=False)

    def sendtoQueue(self, data, name, modifiedDate):
        new_id = random.randint(0, 1000000000)
        while new_id in self.memoId:
            new_id = random.randint(0, 1000000000)
        self.memoId.append(new_id)
        try:
            last_data = self.loadQueue()
            self.status.append({
                "id": new_id,
                "modifier": name,
                "status": "in Queue",
                "modified date": modifiedDate,
                "external model": "undefined",
                "local model": "undefined"

            })
            self.saveStatus(self.status)

        except Exception as e:
            print(
                f"Nav :there is an Error with Queue.json; {e}")
            return
        data["id"] = new_id
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

    def saveStatus(self, status):
        try:
            last_data = self.LastsStatus()
            last_data["Status"] = status
            last_data["memoId"] = self.memoId
            last_data["localPending"] = self.localPending
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
                last_data["Data"].append(data)
                with open(os.path.join(InputPath, f"{name}.json"), 'w', encoding='utf-8') as file:
                    json.dump(last_data, file, indent=4, ensure_ascii=False)
        except:
            print(f"{name}.json is not where it sould be at {InputPath}")

        if self.snailActive:
            self.waitingForLocal = True
            print("Snail: checking the local output")
        else:
            print(f"item with id of ({data["id"]}) has been sent to Local AI")
            self.privateLoopWating = True
            self.createPrivateLoop()

    # /home/alireza/PYTHON/Ecovision/services/Local_AI_Models/InputData/news.json

    def createPrivateLoop(self):
        print("snail was not active; creating a private loop for getting local output")
        time.sleep(2)
        print("PrivateLoop: checking the local output")
        while self.privateLoopWating:
            time.sleep(10)
            self.checkLocalOutput()

    def geminiAnalyze(self, data):
        self.gemini_inprocess = True
        try:
            print("data has been sent to External AI")
            self.result = gemini.analyze(data)
            if self.result != None:
                extract.ex.geminiMx1(self.result)
            else:
                print(f"analyze failed canceled saving")
                self.gemini_inprocess = False
                return False
        except Exception as e:
            print(f"analyze failed canceled saving: {e}")
            self.gemini_inprocess = False
            return False
        self.gemini_inprocess = False
        return True

    def priceAnalyze(self, target=False):
        print("starting for price Opinion proccess...")
        if self.priceAnalyzeActive or target:
            if not self.priceAnalyze_inprocess:
                self.priceAnalyze_inprocess = True
                data = []
                geckoData = gecko.read("FullTimeCrypto")["CryptoData"]
                bonbastData = bonbast.load("FullTimeCurrency.json")[
                    "PriceData"]

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

                GeminiResponse = gemini.priceDetermine(data)
                if GeminiResponse and GeminiResponse.candidates:
                    try:
                        date = datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S")
                        mdText = GeminiResponse.text
                        mdhtmlText = mdText[11:-4]
                        prcmarkdown.priceOp(mdhtmlText, date)
                        navigation.nav.saveOpinion("PriceOp", date, mdText)
                    except Exception as e:
                        print(f"Failed to extract and save opinion: {e}")
                self.priceAnalyze_inprocess = False


az = Analyze()

