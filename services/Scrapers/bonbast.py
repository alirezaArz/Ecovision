import json
import os
import random
import sys
import time
from datetime import datetime, timedelta, timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from services import analyze as analyze

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "scraped")


def main():
    driver = webdriver.Firefox()
    driver.get("https://www.bon-bast.com/")
    time.sleep(random.randint(5, 20))
    driver.implicitly_wait(5)
    memo = []

    try:
        var = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "table.table-condensed"))
        )
        for item in var:
            memo.append((item.text))
    except Exception as e:
        print(f"bonbast had an error :{e}")
    driver.quit()

    change = []
    for num in 0, 1:
        for item in (memo[num].split('\n')):
            change.append(item)
        change.remove('Code Currency Sell Buy')

    result = {}
    result["date"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    
    for item_line in change:
        parts = item_line.split(' ')

        if not parts or len(parts) < 3:
            continue
        code = parts[0]
        buy = parts[-1]
        sell = parts[-2]
        name_parts = parts[1:-2]
        name = " ".join(name_parts)
        
        result[code] = {'name': name, 'buy': buy, 'sell': sell}
        
    addFullTime(result)
    save(result)


def save(new_data):
    analyze.az.sendtoQueue(new_data)
    last_data = load()
    if new_data:
        last_data["Data"].append(new_data)
        try:
            with open(os.path.join(DATA_PATH, "ScBonbast.json"), "w", encoding="utf-8") as s:
                json.dump(last_data, s, ensure_ascii=False, indent=4)
            print("bonbast done successfully")
        except Exception as e:
            print(f"bonbast: file failed at saving {e}")
            print("bonbast faled")
    else:
        print('bonbast: data is empty, saving canceled')
        print("bonbast failed")


def addFullTime(data):
    LastData = load("FullTimeCurrency.json")
    
    if LastData["PriceData"]:
        if LastData["PriceData"][-1]["time"][:10] == data["time"][:10]:
            LastData["PriceData"][-1] = data
        else:
            LastData["PriceData"].append(data)
    else:
        LastData["PriceData"].append(data)

    with open(os.path.join(DATA_PATH, "FullTimeCurrency.json"), 'w', encoding='utf-8') as file:
        json.dump(LastData, file, indent=4, ensure_ascii=False)



def load(filename="ScBonbast.json"):
    try:
        with open(os.path.join(DATA_PATH, filename), "r", encoding="utf-8") as l:
            data = json.load(l)
            return (data)
    except Exception as e:
        print(
            f"bonbast : {filename} is not where it sould be at {DATA_PATH}   ,,, : {e}")

