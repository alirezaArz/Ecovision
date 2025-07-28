# Eghtesad news
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


def main():
    dic = {}
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Chrome()
    driver.get("https://www.eghtesadnews.com/")

    time.sleep(3)
    try:
        div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.content.webgardi-box'))
        )

    except Exception as e:
        print(f"esdn had an error at :{e}")

    titles = div.find_elements(By.TAG_NAME, "a")
    titles = titles[1:-1]

    for i in range(len(titles)):
        titles[i] = titles[i].text

    titles = [i.replace("\u200c", " ") for i in titles]

    for i in range(len(titles)):
        dic[i] = titles[i]

    driver.quit()

    save(dic)


def search(inp_arg):
    dic = {}
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Firefox()
    driver.get("https://www.eghtesadnews.com/newsstudios/search")

    time.sleep(3)
    try:
        inp = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'query'))
        )

    except Exception as e:
        print(f"esdn had an error at :{e}")

    inp.click()
    inp.send_keys(inp_arg)
    inp.send_keys(Keys.RETURN)

    try:
        titles = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".fnb.fn15.clr04.ng-binding"))
        )
    except Exception as e:
        print(f"esdn had an error at : {e}")

    for i in range(len(titles)):
        dic[i] = titles[i].text

    driver.quit()

    save(dic)


def save(new_data):
    analyze.az.sendtoQueue(new_data, "nyTimes", new_data["date"])
    last_data = load()
    if new_data:
        last_data["Data"].append(new_data)
        try:
            with open(os.path.join(DATA_PATH, "ScEghtsdNews.json"), "w", encoding="utf-8") as s:
                json.dump(last_data, s, ensure_ascii=False, indent=4)
            print("esdn done successfully")
        except:
            print("esdn: file failed at saving")
            print("esdn faled")
    else:
        print('esdn: data is empty, saving canceled')
        print("esdn failed")


def load(filename="ScEghtsdNews.json"):
    try:
        with open(os.path.join(DATA_PATH, "ScEghtsdNews.json"), "r", encoding="utf-8") as l:
            data = json.load(l)
        return (data)
    except:
        print(
            f"esdn : Eghtesat_news.json is not where it sould be at {DATA_PATH}")


# ----------------------------- testing analyze manager --------------------------------

a2 = {
    "date": "2025-07-26 22:13:26",
            "0": {
                "title": "How Trump’s Attacks on the Fed Chair Have Intensified",
                "summary": "President Trump has targeted Jerome H. Powell on more than 70 separate occasions, more than half of them since April. His statements fall into four broad categories."
            },
    "1": {
                "title": "Trump Spars With Powell Over Fed’s Costly Renovations in Rare Visit",
                "summary": "The administration has repeatedly criticized Jerome H. Powell, the chair of the central bank, for his handling of the economy and the cost of work on the institution’s headquarters."
            },
    "2": {
                "title": "‘Unprecedented’ Investment Fund Seals Deal for Japan and Expands Trump’s Influence",
                "summary": "President Trump will get to decide where to invest Japanese money and the United States will keep 90 percent of the profits, the White House said."
            }
}

# -------test--------

#analyze.az.sendtoQueue(a2, "esdn", "2025-07-27 01:16:29")
