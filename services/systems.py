import sys
import os
import json
from datetime import datetime
import random
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
        self.percentage = gecko.read('percentage')

    def gecko_read(self,name):
        with open(os.path.join(GECKO_PATH, f"gecko{name}.json"), 'r', encoding='utf-8') as file:
            data = json.load(file)
            return(data)
    def getStatGeckoPrice(self):
        self.priceData = self.gecko_read('price')
        print(self.priceData)
        self.result = [
        { "symbol": "BTC", "name": "Bitcoin", "price": self.priceData[-1]['bitcoin']['usd'] , "change": f"{self.percentage['bitcoin']}%", "positive": self.percentage['pos1'] },
        { "symbol": "ETH", "name": "Ethereum", "price": self.priceData[-1]['ethereum']['usd'], "change": f"{self.percentage['ethereum']}%", "positive": self.percentage['pos4'] },
        { "symbol": "ADA", "name": "Cardano", "price": self.priceData[-1]['cardano']['usd'], "change": f"{self.percentage['cardano']}%", "positive": self.percentage['pos2'] },
        { "symbol": "SOL", "name": "Solana", "price": self.priceData[-1]['solana']['usd'], "change": f"{self.percentage['solana']}%", "positive": self.percentage['pos5'] },
        { "symbol": "USDT", "name": "Tether", "price": self.priceData[-1]['tether']['usd'], "change": f"{self.percentage['tether']}%", "positive": self.percentage['pos6'] },
        { "symbol": "DOGE", "name": "Dogecoin", "price": self.priceData[-1]['dogecoin']['usd'], "change": f"{self.percentage['dogecoin']}%", "positive": self.percentage['pos3'] },
        ]
        return self.result


    def get_snail_data(self):
        snaildata = snail.snail.snailread()
        return snaildata
        
            


vgsy = System()

