import sys
import os
import json
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from services.APIs import gecko as gecko
from services.Scrapers import bonbast as bonbast
from services import snail as snail

GECKO_PATH = os.path.join(project_root, 'services', 'APIs', 'geckoData')
NYTIME_PATH = os.path.join(project_root, 'services', 'scrapers', 'nytimesDATA')

class System():
    def __init__(self):
        pass

    def gecko_read(self,name):
        with open(os.path.join(GECKO_PATH, f"gecko{name}.json"), 'r', encoding='utf-8') as file:
            data = json.load(file)
            return(data)
        
    def getStatGeckoPrice(self):
        self.priceData = self.gecko_read('price')
        self.result = [
        { "symbol": "BTC", "name": "Bitcoin", "price": self.priceData['bitcoin']['usd'] , "change": "+2.4%", "positive": True },
        { "symbol": "ETH", "name": "Ethereum", "price": self.priceData['ethereum']['usd'], "change": "+1.8%", "positive": True },
        { "symbol": "ADA", "name": "Cardano", "price": self.priceData['cardano']['usd'], "change": "-0.9%", "positive": False },
        { "symbol": "SOL", "name": "Solana", "price": self.priceData['solana']['usd'], "change": "+3.2%", "positive": True },
        { "symbol": "USDT", "name": "Tether", "price": self.priceData['tether']['usd'], "change": "-1.2%", "positive": False },
        { "symbol": "DOGE", "name": "Dogecoin", "price": self.priceData['dogecoin']['usd'], "change": "+0.7%", "positive": True },
        ]
        return self.result


    def get_snail_data(self):
        snailData = snail.snail.lead()
        for item in snailData.keys():
            snailData[item]["id"] = item
            snailData[item]["image"] = "placeholder.svg"
        return(snailData)
    
        


vgsy = System()



print(vgsy.get_snail_data())