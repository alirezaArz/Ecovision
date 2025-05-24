import requests
    
def is_online(test_url="https://www.google.com"):
    try:
        response = requests.get(test_url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def connect(url, params):

    try:
        if params != {}:
            response = requests.get(url, params=params)
        else:
            response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        
        elif response.status_code == 429:
            return 'to many requests'
        elif response.status_code == 404:
            return 'wrong url or params'
        else:
            return ("unknown error", response.status_code)

    except requests.exceptions.RequestException:
        return "unable to connect to the coingecko , check your connection and try again"


def price(ids:set, vs_currencies:set):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
    'ids': ','.join(ids),
    'vs_currencies': ','.join(vs_currencies),
    }
    return connect(url, params)



def market_chart(vs_currency:set, days:int):
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {
        'vs_currency': ','.join(vs_currency),
        'days': str(days),
    }
    if days <= 90:        
        return connect(url, params)
    else:
        days = 90
        return connect(url, params)

def ticker(ids:set):
    url = f"https://api.coingecko.com/api/v3/coins/{','.join(ids)}/tickers"
    params = {}
    return connect(url, params)

def markets(vs_currency:set, order= 'market_cap_desc'):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc"
    params = {
        'vs_currency': ','.join(vs_currency),
        'order': ','.join(order)
    }
    return connect(url, params)

def trends():
    url = "https://api.coingecko.com/api/v3/search/trending"
    params = {}
    return connect(url, params)

def globals():
    url = "https://api.coingecko.com/api/v3/global"
    params = {}
    return connect(url, params)


#print(price({'bitcoin'}, {'usd'}))
#print(market_chart({'usd'}, 2))
#print(is_online())
#print(ticker({'bitcoin'}))
#print(markets({'usd'}))
#print(trends())
#print(globals())