import json
import os
import sys
from datetime import datetime, timedelta, timezone

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'geckoData')


def save(name: str, response: json):
    try:
        last_result = read("price")
        response.update({"time": datetime.now(
        ).strftime("%Y-%m-%d %H:%M:%S")})
        last_result.append(response)
        sendingData = last_result
    except FileNotFoundError as e:
        print(f"no previous save! {e}")
        sendingData = []
        response.update({"time": datetime.now(
        ).strftime("%Y-%m-%d %H:%M:%S")})
        sendingData.append(response)
    addFullTime(response)
    with open(os.path.join(DATA_PATH, f"{name}"), 'w', encoding='utf-8') as file:
        json.dump(sendingData, file, indent=4, ensure_ascii=False)
        file.write("\n")
        print("saved")

    old_clean(name)


def addFullTime(data):
    LastData = read("FullTimeCrypto")
    if LastData["CryptoData"]:
        if LastData["CryptoData"][-1]["time"][:10] == data["time"][:10]:
            LastData["CryptoData"][-1] = data
        else:
            LastData["CryptoData"].append(data)
    else:
        LastData["CryptoData"].append(data)

    with open(os.path.join(DATA_PATH, "geckoFullTimeCrypto.json"), 'w', encoding='utf-8') as file:
        json.dump(LastData, file, indent=4, ensure_ascii=False)


def read(name):
    with open(os.path.join(DATA_PATH, f"gecko{name}.json"), 'r', encoding='utf-8') as file:
        data = json.load(file)
        return (data)


def old_clean(name: str):
    to_be_deleted = []
    nowww_time = datetime.now()

    with open(os.path.join(DATA_PATH, f"{name}"), 'r', encoding='utf-8') as file:
        list_of_dicts = json.load(file)

        for data_dict in list_of_dicts:

            time_str = str(data_dict["time"])
            timestamp_dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            delta = nowww_time - timestamp_dt
            if delta > timedelta(hours=24):
                to_be_deleted.append(data_dict)

        for trash in to_be_deleted:
            list_of_dicts.remove(trash)

        with open(os.path.join(DATA_PATH, f"{name}"), 'w', encoding='utf-8') as file:
            json.dump(list_of_dicts, file, indent=4, ensure_ascii=False)


def is_online(test_url="https://www.google.com"):
    try:
        response = requests.get(test_url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def connect(url, params, id: str):
    print("Gecko is running")
    try:
        if params != {}:
            response = requests.get(url, params=params)
            print(response.status_code)
        else:
            response = requests.get(url)

        if response.status_code == 200:
            save(id, response.json())
            percentage()
            return response.json()

        elif response.status_code == 429:

            return 'to many requests'
        elif response.status_code == 404:

            return 'wrong url or params'
        else:

            return ("unknown error", response.status_code)

    except requests.exceptions.ConnectionError as e:
        print(
            f"unable to connect to the coingecko , check your connection and try again {e}")


def price(ids: set, vs_currencies: set):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(ids),
        'vs_currencies': ','.join(vs_currencies),
    }
    return connect(url, params, 'geckoprice.json')


def market_chart(vs_currency: set, days: int):
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


def ticker(ids: set):
    url = f"https://api.coingecko.com/api/v3/coins/{','.join(ids)}/tickers"
    params = {}
    return connect(url, params, 'geckoticker.json')


def markets(vs_currency: set, order='market_cap_desc'):
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
    Data = read('price')
    num1 = round(((Data[-1]['bitcoin']['usd'] - Data[0]
                 ['bitcoin']['usd'])/Data[0]['bitcoin']['usd'])*100, 3)
    if num1 < 0:
        pos1 = False
    else:
        pos1 = True
    num2 = round(((Data[-1]['cardano']['usd'] - Data[0]
                 ['cardano']['usd'])/Data[0]['cardano']['usd'])*100, 3)
    if num2 < 0:
        pos2 = False
    else:
        pos2 = True
    num3 = round(((Data[-1]['dogecoin']['usd'] - Data[0]
                 ['dogecoin']['usd'])/Data[0]['dogecoin']['usd'])*100, 3)
    if num3 < 0:
        pos3 = False
    else:
        pos3 = True
    num4 = round(((Data[-1]['ethereum']['usd'] - Data[0]
                 ['ethereum']['usd'])/Data[0]['ethereum']['usd'])*100, 3)
    if num4 < 0:
        pos4 = False
    else:
        pos4 = True
    num5 = round(((Data[-1]['solana']['usd'] - Data[0]
                 ['solana']['usd'])/Data[0]['solana']['usd'])*100, 3)
    if num5 < 0:
        pos5 = False
    else:
        pos5 = True
    num6 = round(((Data[-1]['tether']['usd'] - Data[0]
                 ['tether']['usd'])/Data[0]['tether']['usd'])*100, 3)
    if num6 < 0:
        pos6 = False
    else:
        pos6 = True
    answer = {
        'bitcoin': num1,
        "pos1": pos1,
        'cardano': num2,
        "pos2": pos2,
        'dogecoin': num3,
        "pos3": pos3,
        'ethereum': num4,
        "pos4": pos4,
        'solana': num5,
        "pos5": pos5,
        'tether': num6,
        "pos6": pos6
    }
    with open(os.path.join(DATA_PATH, 'geckopercentage.json'), 'w', encoding='utf-8') as file:
        json.dump(answer, file, indent=4, ensure_ascii=False)


# price({'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'dogecoin'}, {'usd'})
# percentage()
# print(market_chart({'usd'}, 2))
# print(is_online())
# print(ticker({'bitcoin'}))
# print(markets({'usd'}))
# print(trends())
# print(globals())
# print(read('price'))
