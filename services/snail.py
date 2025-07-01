import json
import os
import random
import sys
import time
from datetime import datetime

from halo import Halo

from services.AI import gemeni as gemeni
from services.AI import local as ollama
from services.APIs import gecko as gecko
from services.Scrapers import bloomberg
from services.Scrapers import bonbast as bonbast
from services.Scrapers import dnsd as dnsd
from services.Scrapers import esdn
from services.Scrapers import nytimes as nytimes
from services.Scrapers import yahoo

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
snailpath = os.path.join(project_root, 'services', 'SnailData')
DATA_PATH = os.path.join(project_root, "scraped")


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


class Snail():
    def __init__(self):

        self.spinner = Halo(text='', spinner={
            "interval": 80,
            "frames": [
                "[    ]",
                "[   =]",
                "[  ==]",
                "[ ===]",
                "[====]",
                "[=== ]",
                "[==  ]",
                "[=   ]"
            ]
        })
        self.active = False
        self.analyze_active = False
        self.gemeni_active = False
        self.localai_active = False

        self.bonbast_inprocess = False
        self.dnsd_inprocess = False
        self.nytimes_inprocess = False
        self.yahoo_inprocess = False
        self.gecko_inprocess = False
        self.esdn_inprocess = False
        self.bloomberg_inprocess = False
        self.gemeni_inprocess = False
        self.localai_inprocess = False
        self.durationsBackup = {
        }

    def activate(self, name):
        if name == 'bonbast' and name not in self.durationsBackup:
            self.durationsBackup['bonbast'] = 3000
        elif name == 'dnsd' and name not in self.durationsBackup:
            self.durationsBackup['dnsd'] = 3600
        elif name == 'nytimes' and name not in self.durationsBackup:
            self.durationsBackup['nytimes'] = 3600
        elif name == 'yahoo' and name not in self.durationsBackup:
            self.durationsBackup['yahoo'] = 3600
        elif name == 'gecko' and name not in self.durationsBackup:
            self.durationsBackup['gecko'] = 3000
        elif name == 'esdn' and name not in self.durationsBackup:
            self.durationsBackup['esdn'] = 3600
        elif name == 'bloomberg' and name not in self.durationsBackup:
            self.durationsBackup['bloomberg'] = 3600
        self.durations = self.durationsBackup.copy()
        print(f"{name} has been added to active services")

    def deactivate(self, name):
        if name == 'bonbast' and name in self.durationsBackup:
            del self.durationsBackup['bonbast']
        elif name == 'dnsd' and name in self.durationsBackup:
            del self.durationsBackup['dnsd']
        elif name == 'nytimes' and name in self.durationsBackup:
            del self.durationsBackup['nytimes']
        elif name == 'yahoo' and name in self.durationsBackup:
            del self.durationsBackup['yahoo']
        elif name == 'gecko' and name in self.durationsBackup:
            del self.durationsBackup['gecko']
        elif name == 'esdn' and name in self.durationsBackup:
            del self.durationsBackup['esdn']
        elif name == 'bloomberg' and name in self.durationsBackup:
            del self.durationsBackup['bloomberg']
        self.durations = self.durationsBackup.copy()
        print(f"{name} has been removed from active services")

    def instantrun(self, name='all'):
        self.spinner.start()
        if name == 'all':
            if not self.bonbast_inprocess:
                try:
                    self.bonbast_inprocess = True
                    print("starting bonbast")
                    bonbast.main()
                    self.bonbast_inprocess = False
                except:
                    print("bonbast failed")
                    self.bonbast_inprocess = False

            if not self.dnsd_inprocess:
                try:
                    self.dnsd_inprocess = True
                    print("starting dnsd")
                    dnsd.main()
                    self.dnsd_inprocess = False
                except:
                    print("dnsd failed")
                    self.dnsd_inprocess = False

            if not self.nytimes_inprocess:
                try:
                    self.nytimes_inprocess = True
                    print("starting nytimes")
                    nytimes.main()
                    self.nytimes_inprocess = False
                except:
                    print("nytimes failed")
                    self.nytimes_inprocess = False

            if not self.yahoo_inprocess:
                try:
                    self.yahoo_inprocess = True
                    print("starting yahoo")
                    yahoo.main()
                    self.yahoo_inprocess = False
                except:
                    print("yahoo failed")
                    self.yahoo_inprocess = False
            if not self.gecko_inprocess:
                try:
                    print("starting gecko")
                    self.gecko_inprocess = True
                    gecko.price({'bitcoin', 'ethereum', 'Cardano',
                                'tether', 'Solana', 'dogecoin'}, {'usd'})
                    self.gecko_inprocess = False
                except:
                    print("gecko failed")
                    self.gecko_inprocess = False
            if not self.esdn_inprocess:
                try:
                    self.esdn_inprocess = True
                    print("starting esdn")
                    esdn.main()
                    self.esdn_inprocess = False
                except:
                    print("esdn failed")
                    self.esdn_inprocess = False

            if not self.bloomberg_inprocess:
                try:
                    self.bloomberg_inprocess = True
                    print("starting bloomberg")
                    bloomberg.main()
                    self.bloomberg_inprocess = False
                except:
                    print("bloomberg failed")
                    self.bloomberg_inprocess = False

                try:
                    print("starting snail")
                    self.analyze()
                except:
                    print("analyze failed")

        if name == 'bonbast':
            if not self.bonbast_inprocess:
                try:
                    self.bonbast_inprocess = True
                    print("starting bonbast")
                    bonbast.main()
                    self.bonbast_inprocess = False
                except:
                    print("bonbast failed")
                    self.bonbast_inprocess = False

        if name == 'dnsd':
            if not self.dnsd_inprocess:
                try:
                    self.dnsd_inprocess = True
                    print("starting dnsd")
                    dnsd.main()
                    self.dnsd_inprocess = False
                except:
                    print("dnsd failed")
                    self.dnsd_inprocess = False

        if name == 'nytimes':
            if not self.nytimes_inprocess:
                try:
                    self.nytimes_inprocess = True
                    print("starting nytimes")
                    nytimes.main()
                    self.nytimes_inprocess = False
                except:
                    print("nytimes failed")
                    self.nytimes_inprocess = False
        if name == 'yahoo':
            if not self.yahoo_inprocess:
                try:
                    self.yahoo_inprocess = True
                    print("starting yahoo")
                    yahoo.main()
                    self.yahoo_inprocess = False
                except:
                    print("yahoo failed")
                    self.yahoo_inprocess = False
        if name == 'gecko':
            if not self.gecko_inprocess:
                try:
                    print("starting gecko")
                    self.gecko_inprocess = True
                    gecko.price({'bitcoin', 'ethereum', 'Cardano',
                                'tether', 'Solana', 'dogecoin'}, {'usd'})
                    self.gecko_inprocess = False
                except:
                    print("gecko failed")
                    self.gecko_inprocess = False
        if name == 'esdn':
            if not self.esdn_inprocess:
                try:
                    self.esdn_inprocess = True
                    print("starting esdn")
                    esdn.main()
                    self.esdn_inprocess = False
                except:
                    print("esdn failed")
                    self.esdn_inprocess = False

        if name == "bloomberg":
            if not self.bloomberg_inprocess:
                try:
                    self.bloomberg_inprocess = True
                    print("starting bloomberg")
                    bloomberg.main()
                    self.bloomberg_inprocess = False
                except:
                    print("bloomberg failed")
                    self.bloomberg_inprocess = False

        if name == 'analyze':
            try:
                print("starting analyze")
                self.analyze()
            except:
                print("analyze failed")
        self.spinner.stop()

    def runserver(self):
        try:
            while self.active and self.durations:

                self.next_process_name = min(
                    self.durations, key=lambda k: self.durations[k])
                self.CurrentWaitTime = self.durations[self.next_process_name]
                print(
                    f"\n next process in {int(min(self.durations.values()) / 60)} minutres! > {self.next_process_name}")
                self.spinner.start()

# ---------------------------------------------------------- code space
# code that runs here, runs every time a timer hits 0
# ------------------------------------------------------------

                time.sleep(self.CurrentWaitTime)

                for item in self.durations:
                    val = self.durations[item]

                    self.durations[item] -= self.CurrentWaitTime
                    if self.durations[item] == 0:
                        if item == "bonbast":
                            bonbast.main()
                        elif item == "dnsd":
                            dnsd.main()
                        elif item == "nytimes":
                            nytimes.main()
                        elif item == "yahoo":
                            yahoo.main()
                        elif item == "gecko":
                            gecko.price(
                                {'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'dogecoin'}, {'usd'})
                        elif item == "esdn":
                            esdn.main()
                        elif item == "bloomberg":
                            bloomberg.main()
                        if self.analyze_active == True:
                            self.analyze()
                        self.durations[item] = self.durationsBackup[item]

                print(f" remaining times: {self.durations}")
                self.spinner.stop()
        except:
            self.spinner.stop()
            print('There was no active service in the list, server is shutting down...')
            time.sleep(random.randint(0, 3))
        finally:
            self.spinner.stop()
            print('snail has been deactivated')

    def snailread(self):
        try:
            with open(os.path.join(snailpath, f"Snaildata.json"), 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                return (self.data)
        except:
            print(
                f"snail : Snaildata.json is not where it sould be at {snailpath}")

    def snailsave(self, sfile):
        try:
            try:
                text_content = sfile.candidates[0].content.parts[0].text
                if text_content.startswith("```json"):
                    text_content = text_content[len("```json"):].strip()
                if text_content.endswith("```"):
                    text_content = text_content[:-len("```")].strip()
                snaildata = json.loads(text_content)

                ecocat = ['images/economy/im1.jpg', 'images/economy/im2.jpg', 'images/economy/im3.jpg', 'images/economy/im4.jpg', 'images/economy/im5.jpg', 'images/economy/im6.jpg', 'images/economy/im7.jpg', 'images/economy/im8.jpg', 'images/economy/im9.jpg', 'images/economy/im10.jpg', 'images/economy/im11.jpg', 'images/economy/im12.jpg', 'images/economy/im13.jpg', 'images/economy/im14.jpg', 'images/economy/im15.jpg',
                          'images/economy/im16.jpg', 'images/economy/im17.jpg', 'images/economy/im18.jpg', 'images/economy/im19.jpg', 'images/economy/im20.jpg', 'images/economy/im21.jpg', 'images/economy/im22.jpg', 'images/economy/im23.jpg', 'images/economy/im24.jpg', 'images/economy/im25.jpg', 'images/economy/im26.jpg', 'images/economy/im27.jpg', 'images/economy/im28.jpg', 'images/economy/im29.jpg', 'images/economy/im30.jpg']
                fincat = ['images/finance/im1.jpg', 'images/finance/im2.jpg', 'images/finance/im3.jpg', 'images/finance/im4.jpg', 'images/finance/im5.jpg', 'images/finance/im6.jpg', 'images/finance/im7.jpg',
                          'images/finance/im8.jpg', 'images/finance/im9.jpg', 'images/finance/im10.jpg', 'images/finance/im11.jpg', 'images/finance/im12.jpg', 'images/finance/im13.jpg', 'images/finance/im14.jpg', 'images/finance/im15.jpg']
                invcat = ['images/investing/im1.jpg', 'images/investing/im2.jpg', 'images/investing/im3.jpg', 'images/investing/im4.jpg', 'images/investing/im5.jpg',
                          'images/investing/im6.jpg', 'images/investing/im7.jpg', 'images/investing/im8.jpg', 'images/investing/im9.jpg', 'images/investing/im10.jpg']
                marcat = ['images/markets/im1.jpg', 'images/markets/im2.jpg', 'images/markets/im3.jpg', 'images/markets/im4.jpg', 'images/markets/im5.jpg',
                          'images/markets/im6.jpg', 'images/markets/im7.jpg', 'images/markets/im8.jpg', 'images/markets/im9.jpg', 'images/markets/im10.jpg']
                scicat = ['images/science/im1.jpg', 'images/science/im2.jpg', 'images/science/im3.jpg', 'images/science/im4.jpg', 'images/science/im5.jpg',
                          'images/science/im6.jpg', 'images/science/im7.jpg', 'images/science/im8.jpg', 'images/science/im9.jpg', 'images/science/im10.jpg']
                teccat = ['images/technology/im1.jpg', 'images/technology/im2.jpg', 'images/technology/im3.jpg', 'images/technology/im4.jpg', 'images/technology/im5.jpg',
                          'images/technology/im6.jpg', 'images/technology/im7.jpg', 'images/technology/im8.jpg', 'images/technology/im9.jpg', 'images/technology/im10.jpg']
                output_dict = {}
                output_dict["newsData"] = []
                current_iso_date = datetime.now().isoformat()

                for item_key_str, original_item_data in snaildata.items():
                    transformed_item = {}

                    try:
                        transformed_item["id"] = int(item_key_str) + 1
                    except ValueError:
                        transformed_item["id"] = item_key_str

                    transformed_item["title"] = original_item_data.get(
                        "title", "")
                    transformed_item["summary"] = original_item_data.get(
                        "summary", "")

                    transformed_item["category"] = original_item_data.get(
                        "category", "news")
                    if transformed_item["category"] == "Economy":
                        transformed_item["image"] = random.choice(ecocat)
                    elif transformed_item["category"] == "Finance":
                        transformed_item["image"] = random.choice(fincat)
                    elif transformed_item["category"] == "Investing":
                        transformed_item["image"] = random.choice(invcat)
                    elif transformed_item["category"] == "Markets":
                        transformed_item["image"] = random.choice(marcat)
                    elif transformed_item["category"] == "Science":
                        transformed_item["image"] = random.choice(scicat)
                    elif transformed_item["category"] == "Technology":
                        transformed_item["image"] = random.choice(teccat)

                    transformed_item["importance"] = original_item_data.get(
                        "importance", "medium")
                    transformed_item["date"] = current_iso_date
                    output_dict["newsData"].append(transformed_item)
            except:
                print(
                    "gemeni's result was not in form of needed structure; saving process has been canceled!")
                return
            with open(os.path.join(snailpath, f"Snaildata.json"), 'w', encoding='utf-8') as file:
                json.dump(output_dict, file, indent=4, ensure_ascii=False)
                print("snaildata saved successfully")
        except:
            print("snail: failed at saving file")

    def get_news_data(self):
        data = ""
        # files = [ bloomberg, dnsd, esdn, nytimes, yahoo ]
        data += str(bloomberg.load())
        data += str(dnsd.load())
        data += str(esdn.load())
        data += str(nytimes.load())
        data += str(yahoo.load())
        return (data)

    def analyze(self, core='none'):
        self.entry = self.get_news_data()
        if core == 'gemini' and not self.gemeni_inprocess:
            try:
                if not self.gemeni_inprocess:
                    self.gemeni_inprocess = True
                    self.result = gemeni.analyze(self.entry)
                    if self.result != None:
                        self.snailsave(self.result)
                    else:
                        print("analyze failed, canceled saving")
            except:
                print('analyze failed code:1')
            self.gemeni_inprocess = False

        elif core == 'localai' and not self.localai_inprocess:
            try:
                self.localai_active = True
                self.result = ollama.answer(self.entry)
                # self.snailsave(self.result)
            except:
                print("analyze failed code:2")
            self.localai_inprocess = False

        elif core == 'none':
            if self.gemeni_active and self.localai_active:
                try:
                    if not self.gemeni_inprocess:
                        self.gemeni_inprocess = True
                        self.result = gemeni.analyze(self.entry)
                        if self.result != None:
                            self.snailsave(self.result)
                        else:
                            print("analyze failed, canceled saving")
                except:
                    if not self.localai_active:
                        self.localai_active = True
                        self.result = ollama.answer(self.entry)
                        self.localai_inprocess = False
                    # self.snailsave(self.result)  // snail save doesnt work for this... thats customized for gemini only
                else:
                    print('analyze failed code:3')
                self.gemeni_inprocess = False
                self.localai_inprocess = False

            elif self.gemeni_active and not self.localai_inprocess:
                try:
                    self.gemeni_active = True
                    self.result = gemeni.analyze(self.entry)
                    if self.result != None:
                        self.snailsave(self.result)

                    else:
                        print("analyze failed, canceled saving")
                except:

                    print('analyze failed code:4')
                self.gemeni_inprocess = False
                self.localai_inprocess = False

            elif self.localai_active and not self.localai_active:
                try:
                    self.localai_active = True
                    self.result = ollama.answer(self.entry)
                    # self.snailsave(self.result)
                except:
                    print("analyze failed code:5")
                self.gemeni_inprocess = False
                self.localai_inprocess = False
            else:
                self.gemeni_inprocess = False
                self.localai_inprocess = False
                print("no AI core is active, please activate one")


snail = Snail()
# snail.runserver()
# snail.instantrun(['yahoo','gecko', 'esdn', 'bloomberg'])
