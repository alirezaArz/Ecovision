import json
import os
import time
from datetime import datetime, timedelta, timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from services import analyze as analyze

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "scraped")

options = Options()
options.add_argument("--headless")


def main(command=False):
    dic = {}
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Chrome()
    driver.get("https://finance.yahoo.com/")

    time.sleep(3)
    bdy = driver.find_element(By.TAG_NAME, "body")
    for i in range(60):
        bdy.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.1)

    try:
        var = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "h3"))
        )

    except Exception as e:
        print(f"yahoo had an error : {e}")

    titles = []
    for i in var:
        if len(i.text) > 20:
            titles.append(i)

    for i in range(len(titles)):
        dic[i] = titles[i].text

    driver.quit()
    save(dic, command)


def save(new_data, command=False):
    analyze.az.sendtoQueue(new_data, "yahoo", new_data["date"], command)
    last_data = load()
    if new_data:
        last_data["Data"].append(new_data)
        try:
            with open(os.path.join(DATA_PATH, "ScYahoo.json"), "w", encoding="utf-8") as s:
                json.dump(last_data, s, ensure_ascii=False, indent=4)
            print("yahoo done successfully")
        except:
            print("yahoo: file failed at saving")
            print("yahoo faled")
    else:
        print('yahoo: data is empty, saving canceled')
        print("yahoo failed")


def load(filename="ScYahoo.json"):
    try:
        with open(os.path.join(DATA_PATH, "ScYahoo.json"), "r", encoding="utf-8") as l:
            data = json.load(l)
        return (data)
    except:
        print(f"yahoo : ScYahoo.json is not where it sould be at {DATA_PATH}")
