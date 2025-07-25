from datetime import datetime
import json
import os
import random
import time
from datetime import datetime, timedelta, timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--headless")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "scraped")


def main():
    dic = {}
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Firefox()
    driver.get("https://www.nytimes.com/section/business/economy")
    time.sleep(random.randint(5, 20))
    driver.implicitly_wait(5)

    titles_elements = []
    descript_elements = []

    try:
        titles_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.e15t083i0'))
        )
        descript_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.css-1pga48a.e15t083i1'))
        )
    except Exception as e:
        print(f"nytimes had an error fetching elements : {e}")

    if titles_elements and descript_elements:
        num_items = min(len(titles_elements), len(descript_elements))

        for i in range(num_items):
            item_data = {
                "title": titles_elements[i].text,
                "summary": descript_elements[i].text,
            }
            dic[i] = item_data

    save(dic)
    driver.quit()


def search(inp_arg):
    dic = {}
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Firefox()
    driver.get("https://www.nytimes.com/")
    time.sleep(random.randint(5, 20))
    driver.implicitly_wait(15)

    try:
        btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.css-tkwi90.e1iflr850'))
        )
    except Exception as e:
        print(f"nytimes had an error : {e}")
        driver.quit()
        return dic

    btn.click()

    time.sleep(1)
    try:
        inp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'query'))
        )
    except Exception as e:
        print(f"nytimes had an error : {e}")
        driver.quit()
        return dic

    inp.click()
    inp.send_keys(f"{inp_arg}")
    inp.send_keys(Keys.RETURN)

    time.sleep(3)

    titles = []
    paras = []
    try:
        titles = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.css-nsjm9t'))
        )

        paras = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.css-e5tzus'))
        )
    except Exception as e:
        print(f"nytimes had an error : {e}")

    if titles and paras:
        num_results = min(len(titles), len(paras))
        temp_results = []
        for i in range(num_results):
            temp_results.append(titles[i].text + ",," + paras[i].text)
        if temp_results:
            dic = {"search_results": temp_results}

    save(dic)


def save(new_data):
    last_data = load()
    if new_data:
        last_data["Data"].append(new_data)
        try:
            with open(os.path.join(DATA_PATH, "ScNyt.json"), "w", encoding="utf-8") as s:
                json.dump(last_data, s, ensure_ascii=False, indent=4)
            print("nytimes done successfully")
        except Exception as e:
            print(f"nytimes: file failed at saving {e}")
            print("nytimes faled")
    else:
        print('nytimes: data is empty, saving canceled')
        print("nytimes failed")


def load():
    try:
        with open(os.path.join(DATA_PATH, "ScNyt.json"), "r", encoding="utf-8") as l:
            data = json.load(l)
        return (data)
    except Exception as e:
        print(
            f"nytimes : ScNyt.json is not where it sould be at {DATA_PATH} ,,, : {e}")
