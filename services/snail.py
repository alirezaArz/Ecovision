from services import navigation as navigation
from services.Scrapers import yahoo
from services.Scrapers import nytimes as nytimes
from services.Scrapers import esdn
from services.Scrapers import dnsd as dnsd
from services.Scrapers import bonbast as bonbast
from services.Scrapers import bloomberg
from services.APIs import gecko as gecko
from services.External_AI_Models import gemini as gemini
from services import analyze as analyze
import os
import random
import sys
import time
from halo import Halo
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = os.path.join(project_root, "scraped")

if project_root not in sys.path:
    sys.path.insert(0, project_root)


class Snail():
    def __init__(self):

        self.spinner = Halo(text='', spinner={
            "interval": 80,
            "frames": [
                "◜",
                "◠",
                "◝",
                "◞",
                "◡",
                "◟"
            ]
        })
        self.active = False
        self.bonbast_inprocess = False
        self.dnsd_inprocess = False
        self.nytimes_inprocess = False
        self.yahoo_inprocess = False
        self.gecko_inprocess = False
        self.esdn_inprocess = False
        self.bloomberg_inprocess = False
        self.durationsBackup = {
        }

    def val_to_second(self, val, unit):
        result = 0
        if unit == 'sec':
            result = val
        if unit == 'min':
            result = val * 60
        if unit == 'hr':
            result = val * 3600
        if unit == 'day':
            result = val * 86400
        if unit == 'week':
            result = val * 604800
        return result

    def activate(self, name, cycle):
        if cycle:
            val = int(cycle["number"])
            unit = cycle["unit"]
            firstVal = val
            val = self.val_to_second(val, unit)
        else:
            print(
                f"no val has been detected for activating the {name} setting 3600 as default")
            val = 3600
            firstVal = val
            unit = 'sec'

        if name == 'gecko' and name not in self.durationsBackup:
            self.durationsBackup['gecko'] = val
        elif name == 'bonbast' and name not in self.durationsBackup:
            self.durationsBackup['bonbast'] = val
        elif name == 'dnsd' and name not in self.durationsBackup:
            self.durationsBackup['dnsd'] = val
        elif name == 'nytimes' and name not in self.durationsBackup:
            self.durationsBackup['nytimes'] = val
        elif name == 'yahoo' and name not in self.durationsBackup:
            self.durationsBackup['yahoo'] = val
        elif name == 'esdn' and name not in self.durationsBackup:
            self.durationsBackup['esdn'] = val
        elif name == 'bloomberg' and name not in self.durationsBackup:
            self.durationsBackup['bloomberg'] = val
        elif name == 'analyze' and name not in self.durationsBackup:
            self.durationsBackup['analyze'] = val
        elif name == 'priceAnalyze' and name not in self.durationsBackup:
            self.durationsBackup['priceAnalyze'] = val
        elif name == 'gemini' and name not in self.durationsBackup:
            self.durationsBackup['gemini'] = val
        elif name == 'localAi' and name not in self.durationsBackup:
            self.durationsBackup['localAi'] = val

        self.durations = self.durationsBackup.copy()
        print(
            f"{name} has been added to active services in a cycle of {firstVal} {unit}")
        print(f" durations: {self.durationsBackup}")
        self.LogNextDuration()

    def deactivate(self, name):
        if name == 'gecko' and name in self.durationsBackup:
            del self.durationsBackup['gecko']
        elif name == 'bonbast' and name in self.durationsBackup:
            del self.durationsBackup['bonbast']
        elif name == 'dnsd' and name in self.durationsBackup:
            del self.durationsBackup['dnsd']
        elif name == 'nytimes' and name in self.durationsBackup:
            del self.durationsBackup['nytimes']
        elif name == 'yahoo' and name in self.durationsBackup:
            del self.durationsBackup['yahoo']
        elif name == 'esdn' and name in self.durationsBackup:
            del self.durationsBackup['esdn']
        elif name == 'bloomberg' and name in self.durationsBackup:
            del self.durationsBackup['bloomberg']
        elif name == 'analyze' and name in self.durationsBackup:
            del self.durationsBackup['analyze']
        elif name == 'priceAnalyze' and name in self.durationsBackup:
            del self.durationsBackup['priceAnalyze']
        elif name == 'gemini' and name in self.durationsBackup:
            del self.durationsBackup['gemini']
        elif name == 'localAi' and name in self.durationsBackup:
            del self.durationsBackup['localAi']
        self.durations = self.durationsBackup.copy()
        print(f"{name} has been removed from active services")
        print(f" durations: {self.durationsBackup}")
        self.LogNextDuration()

    def instantrun(self, name='all'):
        self.spinner.start()
        if name == 'all':
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
                    dnsd.main(True)
                    self.dnsd_inprocess = False
                except:
                    print("dnsd failed")
                    self.dnsd_inprocess = False

            if not self.nytimes_inprocess:
                try:
                    self.nytimes_inprocess = True
                    print("starting nytimes")
                    nytimes.main(True)
                    self.nytimes_inprocess = False
                except:
                    print("nytimes failed")
                    self.nytimes_inprocess = False

            if not self.yahoo_inprocess:
                try:
                    self.yahoo_inprocess = True
                    print("starting yahoo")
                    yahoo.main(True)
                    self.yahoo_inprocess = False
                except:
                    print("yahoo failed")
                    self.yahoo_inprocess = False

            if not self.esdn_inprocess:
                try:
                    self.esdn_inprocess = True
                    print("starting esdn")
                    esdn.main(True)
                    self.esdn_inprocess = False
                except:
                    print("esdn failed")
                    self.esdn_inprocess = False

            if not self.bloomberg_inprocess:
                try:
                    self.bloomberg_inprocess = True
                    print("starting bloomberg")
                    bloomberg.main(True)
                    self.bloomberg_inprocess = False
                except:
                    print("bloomberg failed")
                    self.bloomberg_inprocess = False
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
                    dnsd.main(True)
                    self.dnsd_inprocess = False
                except:
                    print("dnsd failed")
                    self.dnsd_inprocess = False

        if name == 'nytimes':
            if not self.nytimes_inprocess:
                try:
                    self.nytimes_inprocess = True
                    print("starting nytimes")
                    nytimes.main(True)
                    self.nytimes_inprocess = False
                except:
                    print("nytimes failed")
                    self.nytimes_inprocess = False
        if name == 'yahoo':
            if not self.yahoo_inprocess:
                try:
                    self.yahoo_inprocess = True
                    print("starting yahoo")
                    yahoo.main(True)
                    self.yahoo_inprocess = False
                except:
                    print("yahoo failed")
                    self.yahoo_inprocess = False
        if name == 'esdn':
            if not self.esdn_inprocess:
                try:
                    self.esdn_inprocess = True
                    print("starting esdn")
                    esdn.main(True)
                    self.esdn_inprocess = False
                except:
                    print("esdn failed")
                    self.esdn_inprocess = False

        if name == "bloomberg":
            if not self.bloomberg_inprocess:
                try:
                    self.bloomberg_inprocess = True
                    print("starting bloomberg")
                    bloomberg.main(True)
                    self.bloomberg_inprocess = False
                except:
                    print("bloomberg failed")
                    self.bloomberg_inprocess = False

        if name == 'analyze':
            try:
                print("starting analyze")
                analyze.az.manage()
            except:
                print("analyze failed")
        self.spinner.stop()

    def LogNextDuration(self):
        if self.durations:
            durate_min = min(self.durations.values())
            if durate_min < 60:
                self.duration_min = durate_min
                self.duration_min_unit = "seconds"
            elif 60 <= durate_min < 3600:
                self.duration_min = durate_min / 60
                self.duration_min_unit = "minutes"
            elif 3600 <= durate_min < 86400:
                self.duration_min = durate_min / 3600
                self.duration_min_unit = "hours"
            elif 86400 <= durate_min < 604800:
                self.duration_min = durate_min / 86400
                self.duration_min_unit = "days"
            else:
                self.duration_min = durate_min / 604800
                self.duration_min_unit = "weeks"

            self.next_process_name = min(
                self.durations, key=lambda k: self.durations[k])

            print(
                f"\n next process in {self.duration_min} {self.duration_min_unit}! > {self.next_process_name}")

    def runserver(self):
        self.durations = self.durationsBackup.copy()
        try:
            if self.durations == {}:
                print(
                    f'There was no active service in the list, server is shutting down...')
                self.active = False
                analyze.az.snailActive = False
            while self.active and self.durations:
                analyze.az.snailActive = True

                self.next_process_name = min(
                    self.durations, key=lambda k: self.durations[k])
                self.CurrentWaitTime = self.durations[self.next_process_name]
                self.LogNextDuration()
                self.spinner.start()

# ---------------------------------------------------------- code space
# code that runs here, runs every time a timer hits 0
# ------------------------------------------------------------
                for cnt in range(self.CurrentWaitTime // 10):
                    if self.active:
                        if analyze.az.waitingForLocal:
                            print("Snail: checking the local output")
                            analyze.az.checkLocalOutput()
                        time.sleep(10)
                    else:
                        analyze.az.snailActive = False
                        break

                if self.active:
                    for item in self.durations:
                        self.durations[item] -= self.CurrentWaitTime
                        if self.durations[item] == 0:
                            if item == "gecko":
                                gecko.price(
                                    {'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'dogecoin'}, {'usd'})
                            elif item == "bonbast":
                                bonbast.main()
                            elif item == "dnsd":
                                dnsd.main()
                            elif item == "nytimes":
                                nytimes.main()
                            elif item == "yahoo":
                                yahoo.main()
                            elif item == "esdn":
                                esdn.main()
                            elif item == "bloomberg":
                                bloomberg.main()
                            elif item == "analyze":
                                analyze.az.manage()
                            elif item == "gemini":
                                analyze.az.manage('external')
                            elif item == "localAi":
                                analyze.az.manage('local')
                            elif item == "priceAnalyze":
                                analyze.az.priceAnalyze(True)
                            self.durations[item] = self.durationsBackup[item]

                    print(f" remaining times: {self.durations}")
                self.spinner.stop()
        except Exception as e:
            self.spinner.stop()
            print(f'There was an error on starting the snail: {e}')
            self.active = False
            analyze.az.snailActive = False
            time.sleep(random.randint(0, 3))
        finally:
            self.spinner.stop()
            self.active = False
            analyze.az.snailActive = False
            print('snail has been deactivated')


snail = Snail()
# snail.runserver()
# snail.instantrun(['yahoo','gecko', 'esdn', 'bloomberg'])
