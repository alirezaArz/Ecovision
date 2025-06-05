import requests
import json
from datetime import datetime, timedelta, timezone
import os
from halo import Halo 
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'geckoData')

spinner = Halo(text='', spinner={
		"interval": 120,
		"frames": [
			"▹▹▹▹▹",
			"▸▹▹▹▹",
			"▹▸▹▹▹",
			"▹▹▸▹▹",
			"▹▹▹▸▹",
			"▹▹▹▹▸"
		]
	})

def save(name:str, response):
    try:
        last_result = read("price")
        last_result.append(response)
        sendingData = last_result
    except:
        print("no previous save!")
        sendingData = []
        response.update({"time" : datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")})
        sendingData.append(response)
    
    with open(os.path.join(DATA_PATH, f"{name}"), 'w', encoding='utf-8') as file:
        json.dump(sendingData, file, indent=4, ensure_ascii=False)
        file.write("\n")

def read(name):
    with open(os.path.join(DATA_PATH, f"gecko{name}.json"), 'r', encoding='utf-8') as file:
        data = json.load(file)
        return(data)
    

def is_online(test_url="https://www.google.com"):
    try:
        response = requests.get(test_url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def connect(url, params, id:str):
    print("Gecko is running")
    spinner.start()
    try:
        if params != {}:
            response = requests.get(url, params=params)
            print(response.status_code)
        else:
            response = requests.get(url)

        if response.status_code == 200:
            save(id, response.json())
            spinner.stop()
            return response.json()
        
        elif response.status_code == 429:
            spinner.stop()
            return 'to many requests'
        elif response.status_code == 404:
            spinner.stop()
            return 'wrong url or params'
        else:
            spinner.stop()
            return ("unknown error", response.status_code)
    
    except requests.exceptions.RequestException:
        spinner.stop()
        return "unable to connect to the coingecko , check your connection and try again"
    

def price(ids:set, vs_currencies:set):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
    'ids': ','.join(ids),
    'vs_currencies': ','.join(vs_currencies),
    }
    return connect(url, params, 'geckoprice.json')



def market_chart(vs_currency:set, days:int):
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {
        'vs_currency': ','.join(vs_currency),
        'days': str(days),
    }
    if days <= 90:        
        return connect(url, params, 'geckomarket_chart.json')
    else:
        days = 90
        return connect(url, params, 'geckomarket_chart.json')

def ticker(ids:set):
    url = f"https://api.coingecko.com/api/v3/coins/{','.join(ids)}/tickers"
    params = {}
    return connect(url, params, 'geckoticker.json')

def markets(vs_currency:set, order= 'market_cap_desc'):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc"
    params = {
        'vs_currency': ','.join(vs_currency),
        'order': ','.join(order)
    }
    return connect(url, params, 'geckomarkets.json')

def trends():
    url = "https://api.coingecko.com/api/v3/search/trending"
    params = {}
    return connect(url, params, 'geckotrends.json')

def globals():
    url = "https://api.coingecko.com/api/v3/global"
    params = {}
    return connect(url, params, 'geckoglobals.json')
def percentage():
    Data = []
    Data.append(read("price"))
    num1 = (Data[0] - Data[-6])/100
    num2 = (Data[1] - Data[-5])/100
    num3 = (Data[2] - Data[-4])/100
    num4 = (Data[3] - Data[-3])/100
    num5 = (Data[4] - Data[-2])/100
    num6 = (Data[5] - Data[-1])/100
    answer = {
        'bitcoin': num1,
        'cardano': num2,
        'dogecoin': num3,
        'ethereum': num4,  
        'solana': num5,
        'tether': num6
    }
    with open (os.path.join(DATA_PATH, 'geckopercentage.json'), 'w', encoding='utf-8') as file:
        json.dump(answer, file, indent=4, ensure_ascii=False)
    
  

price({'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'dogecoin'}, {'usd'})
# percentage()
#print(market_chart({'usd'}, 2))
#print(is_online())
#print(ticker({'bitcoin'}))
#print(markets({'usd'}))
#print(trends())
#print(globals())
#print(read('price'))


# _________________________________________
# def percentage(ids:set, vs_currencies:set):
#     url = "https://api.coingecko.com/api/v3/simple/price"
#     params = {
#         'ids': ','.join(ids),
#         'vs_currencies': ','.join(vs_currencies),
#         'include_24hr_change': 'true'
        
#     }
#     return connect(url, params, 'geckopercentage.json')
# percentage({'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'dogecoin'}, {'usd'})
#__________________________________________
# with open(os.path.join(DATA_PATH, 'geckoprice.json'), 'r', encoding='utf-8') as file:
#     answer = file.read([0],[1],[2],[3],[4],[5],[-1],[-2],[-3],[-4],[-5],[-6])
# with open(os.path.join(DATA_PATH, 'geckoglobals.json'), 'w', encoding='utf-8') as file:
#     save('geckopercentage.json', answer)