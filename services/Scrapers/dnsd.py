# donyayae - eghtesaad
import json
import os
import random
import sys
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


def search(inp_arg):
    dic = {}
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Chrome()
    driver.get("https://donya-e-eqtesad.com/newsstudios/search")
    time.sleep(random.randint(5, 20))
    driver.implicitly_wait(5)

    try:
        var = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'query'))
        )
        var.click()
        var.send_keys(str(inp_arg))
        var.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"{e}")
    time.sleep(2)
    try:
        titles = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'ng-binding'))
        )

    except Exception as e:
        print(f"dnsd had an error at scrapping : {e}")

    for i in range(len(titles)):
        dic[i] = titles[i].text
    driver.quit()
    save(dic)


def main(command=False):
    dic = {}
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Chrome()
    driver.get(
        "https://donya-e-eqtesad.com/%D8%A8%D8%AE%D8%B4-%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF-183")

    time.sleep(random.randint(5, 20))
    driver.implicitly_wait(5)

    try:
        paras = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.lead'))
        )
    except Exception as e:
        print(f"dnsd had an error at search : {e}")

    for i in range(len(paras)):
        dic[i] = paras[i].text.replace(chr(0x200C), " ")
    driver.quit()
    save(dic, command)


def save(new_data, command=False):
    analyze.az.sendtoQueue(new_data, "dnsd", new_data["date"], command)
    last_data = load()
    if new_data:
        last_data["Data"].append(new_data)
        try:
            with open(os.path.join(DATA_PATH, "ScDnsd.json"), "w", encoding="utf-8") as s:
                json.dump(last_data, s, ensure_ascii=False, indent=4)
            print("dnsd done successfully")
        except Exception as e:
            print(f"dnsd: file failed at saving {e}")
            print("dnsd faled")
    else:
        print('dnsd: data is empty, saving canceled')
        print("dnsd failed")


def load(filename="ScDnsd.json"):
    try:
        with open(os.path.join(DATA_PATH, "ScDnsd.json"), "r", encoding="utf-8") as l:
            data = json.load(l)
        return (data)
    except Exception as e:
        print(
            f"dnsd : ScDnsd.json is not where it sould be at {DATA_PATH}: {e}")
