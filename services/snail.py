from services import navigation as navigation
from services.Scrapers import yahoo
from services.Scrapers import nytimes as nytimes
from services.Scrapers import esdn
from services.Scrapers import dnsd as dnsd
from services.Scrapers import bonbast as bonbast
from services.Scrapers import bloomberg
from services.APIs import gecko as gecko
from services.External_AI_Models import gemeni as gemeni
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
        

        self.bonbast_inprocess = False
        self.dnsd_inprocess = False
        self.nytimes_inprocess = False
        self.yahoo_inprocess = False
        self.gecko_inprocess = False
        self.esdn_inprocess = False
        self.bloomberg_inprocess = False
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
                    analyze.az.MainDataAnalyze()
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
                analyze.az.MainDataAnalyze()
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
                            analyze.az.MainDataAnalyze()
                        self.durations[item] = self.durationsBackup[item]

                print(f" remaining times: {self.durations}")
                self.spinner.stop()
        except KeyboardInterrupt:
            self.spinner.stop()
            print('There was no active service in the list, server is shutting down...')
            time.sleep(random.randint(0, 3))
        finally:
            self.spinner.stop()
            print('snail has been deactivated')



snail = Snail()
# snail.runserver()
# snail.instantrun(['yahoo','gecko', 'esdn', 'bloomberg'])
