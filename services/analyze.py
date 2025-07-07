import json
import os
import random
import re
import sys
import time
from datetime import datetime, timedelta, timezone

from services import extract as extract
from services import navigation as navigation
from services import systems as system
from services.AI import colab as ollama
from services.AI import gemeni as gemeni
from services.APIs import gecko as gecko
from services.Scrapers import bloomberg
from services.Scrapers import bonbast as bonbast
from services.Scrapers import dnsd as dnsd
from services.Scrapers import esdn
from services.Scrapers import nytimes as nytimes
from services.Scrapers import yahoo


class Analyze():
    def __init__(self):
        self.gemeni_inprocess = False
        self.localai_inprocess = False
        self.gemeni_active = False
        self.localai_active = False

    def get_news_data(self):
        data = ""
        # files = [ bloomberg, dnsd, esdn, nytimes, yahoo ]
        data += str(bloomberg.load())
        data += str(dnsd.load())
        data += str(esdn.load())
        data += str(nytimes.load())
        data += str(yahoo.load())
        return (data)

    def MainDataAnalyze(self, core='none'):
        self.entry = self.get_news_data()
        if core == 'gemini' and not self.gemeni_inprocess:
            try:
                if not self.gemeni_inprocess:
                    self.gemeni_inprocess = True
                    self.result = gemeni.analyze(self.entry)
                    if self.result != None:
                        extract.ex.geminiMx1(self.result)
                    else:
                        print("analyze failed, canceled saving")
            except Exception as e:
                print(f'analyze failed code:1 {e}')
            self.gemeni_inprocess = False

        elif core == 'localai' and not self.localai_inprocess:
            print(2)
            try:
                self.localai_active = True
                self.result = ollama.get_ai_response(self.entry)
                if self.result != None:
                    extract.ex.geminiMx1(self.result)
                else:
                    print("analyze failed, canceled saving")
            except Exception as e:
                print(f"analyze failed code:2 {e}")
            self.localai_inprocess = False

        elif core == 'none':
            if self.gemeni_active and self.localai_active:
                try:
                    if not self.gemeni_inprocess:
                        self.gemeni_inprocess = True
                        self.result = gemeni.analyze(self.entry)
                        if self.result != None:
                            extract.ex.geminiMx1(self.result)
                        else:
                            print("analyze failed, canceled saving")
                except Exception as e:
                    if not self.localai_active:
                        self.localai_active = True
                        self.result = ollama.get_ai_response(self.entry)
                        self.localai_inprocess = False
                        extract.ex.geminiMx1(self.result)
                else:
                    print('analyze failed code:3')
                self.gemeni_inprocess = False
                self.localai_inprocess = False

            elif self.gemeni_active and not self.localai_inprocess:
                try:
                    self.gemeni_active = True
                    self.result = gemeni.analyze(self.entry)
                    if self.result != None:
                        extract.ex.geminiMx1(self.result)

                    else:
                        print("analyze failed, canceled saving")
                except Exception as e:
                    print(f"analyze failed code:4, {e}")
                    self.gemeni_inprocess = False
                    self.localai_inprocess = False

            elif self.localai_active and not self.localai_inprocess:
                try:
                    self.localai_active = True
                    self.result = ollama.get_ai_response(self.entry)
                    extract.ex.geminiMx1(self.result)
                except Exception as e:
                    print(f"analyze failed code:5 {e}")
                self.gemeni_inprocess = False
                self.localai_inprocess = False
            else:
                self.gemeni_inprocess = False
                self.localai_inprocess = False
                print("no AI core is active, please activate one")

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

        cryptoPast = min(geckoData[:-1], key=lambda item: abs((cryptoLastTime -
                         datetime.strptime(item["time"], "%Y-%m-%d %H:%M:%S")) - target_duration))
        bonbastPast = min(bonbastData[:-1], key=lambda item: abs(
            (bonbastLastTime - datetime.strptime(item["time"], "%Y-%m-%d %H:%M:%S")) - target_duration))

        data.append(cryptoPast)
        data.append(bonbastPast)
        data.append(cryptoLast)
        data.append(bonbastLast)

        GeminiResponse = gemeni.priceDetermine(data)
        if GeminiResponse and GeminiResponse.candidates:
            try:
                text_content = GeminiResponse.text
                newResult = {
                    "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                    "opinion": text_content  # Storing the cleaned text
                }

                LastData = navigation.nav.Navread("PriceOpinion")

                LastData["OpinionData"].append(newResult)  # Corrected from .appned

                navigation.nav.saveNavigation(LastData, "PriceOpinion")
                print("Successfully updated PriceOpinion.")

            except Exception as e:
                print(f"Failed to extract and save opinion: {e}")

az = Analyze()

