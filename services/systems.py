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
        images = ["images/im2.jpg", "images/im3.jpg", "images/im4.jpg", "images/im5.jpg"]
        snailData_from_read = snail.snail.snailread()
        
        output_dict = {}
        output_dict["newsData"] = []
        
        current_iso_date = datetime.now().isoformat()

        for item_key_str, original_item_data in snailData_from_read.items():
            transformed_item = {}
            
            try:
                transformed_item["id"] = int(item_key_str) + 1
            except ValueError:
                transformed_item["id"] = item_key_str 
            
            transformed_item["title"] = original_item_data.get("title", "")
            transformed_item["summary"] = original_item_data.get("summary", "")
            transformed_item["image"] = "images/im3.jpg"
            transformed_item["category"] = original_item_data.get("category", "news")
            transformed_item["importance"] = original_item_data.get("importance", "medium")
            transformed_item["date"] = current_iso_date
            
            output_dict["newsData"].append(transformed_item)
                
        return output_dict
        
            


vgsy = System()

