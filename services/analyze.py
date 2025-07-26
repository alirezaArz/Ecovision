import json
import os
import random
import re
import sys
import time
from datetime import datetime, timedelta, timezone

from services.External_AI_Models import extract as extract
from services import navigation as navigation
from services import systems as system
from temp import colab as ollama
from services.External_AI_Models import gemeni as gemeni
from services.APIs import gecko as gecko
from services.Scrapers import bloomberg
from services.Scrapers import bonbast as bonbast
from services.Scrapers import dnsd as dnsd
from services.Scrapers import esdn
from services.Scrapers import nytimes as nytimes
from services.Scrapers import yahoo
from services.Data.markdowns import MkPriceOp as prcmarkdown


class Analyze:
    def __init__(self):
        self.gemeni_inprocess = False
        self.localai_inprocess = False
        self.gemeni_active = False
        self.localai_active = False


    def manage(self):
        pass




    def get_news_data(self):
        data = ""
        # files = [ bloomberg, dnsd, esdn, nytimes, yahoo ]
        data += str(bloomberg.load())
        data += str(dnsd.load())
        data += str(esdn.load())
        data += str(nytimes.load())
        data += str(yahoo.load())
        return data

    def geminiAnalyze(self):
        self.entry = self.get_news_data()
        try:
            if not self.gemeni_inprocess:
                self.gemeni_inprocess = True
                self.result = gemeni.analyze(self.entry)
            if self.result != None:
                extract.ex.geminiMx1(self.result)
            else:
                print("analyze failed, canceled saving")
        except Exception as e:
            print(f"analyze failed code:1 {e}")
        self.gemeni_inprocess = False



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
