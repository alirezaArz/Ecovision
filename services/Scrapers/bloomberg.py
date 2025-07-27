import json
import os
import time
from datetime import datetime, timedelta, timezone
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from services import analyze as analyze

options = Options()
options.add_argument("--headless")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "scraped")


def main():
    dic = {}
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Chrome()
    driver.get("https://www.bloomberg.com/economics")

    try:
        iframe_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "sp_message_iframe_1135992"))
        )
        print("bloomberg : frame found. Switching to iframe...")

        driver.switch_to.frame(iframe_element)
        print("bloomberg : Successfully switched to iframe.")

        refusal_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@title='No, I Do Not Accept' and @aria-label='No, I Do Not Accept']"))
        )
        refusal_button.click()
        print("bloomberg : pressed the button")

        driver.switch_to.default_content()
        print("bloomberg : Switched back to default content.")

        print("bloomberg : switched back from the fuckframe.")
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(
                (By.ID, "sp_message_iframe_1135992"))
        )
    except Exception as e:
        print(f"bloomberg had an error : {e}")

    bdy = driver.find_element(By.TAG_NAME, "body")
    for i in range(5):
        bdy.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.3)
    try:
        sect = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'archive_story_list'))
        )

    except Exception as e:
        print(f"bloomberg had an error : {e}")

    btn = sect.find_element(By.NAME, "outlined-button")
    btn.click()
    time.sleep(3)
    for i in range(7):
        bdy.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.2)

    titles = sect.find_elements(By.TAG_NAME, "span")
    titles = titles[:-4]
    titles2 = []
    for title in titles:
        if len(title.text) > 20:
            titles2.append(title)

    for i in range(len(titles2)):
        dic[i] = titles2[i].text

    driver.quit()

    save(dic)


def search(inp_arg: str):
    dic = {}
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    dic["date"] = current_time
    driver = webdriver.Firefox()
    arg = inp_arg.replace(" ", "%20")
    driver.get(f"https://www.bloomberg.com/search?query={arg}")

    time.sleep(3)

    try:
        iframe_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, "sp_message_iframe_1135992"))
        )
        print("bloomberg : frame found. Switching to iframe...")

        driver.switch_to.frame(iframe_element)
        print("bloomberg : Successfully switched to iframe.")

        refusal_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@title='No, I Do Not Accept' and @aria-label='No, I Do Not Accept']"))
        )
        refusal_button.click()
        print("bloomberg : pressed the button")

        driver.switch_to.default_content()
        print("bloomberg : Switched back to default content.")

        print("bloomberg : switched back from the fuckframe.")
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(
                (By.ID, "sp_message_iframe_1135992"))
        )
    except Exception as e:
        print(f"bloomberg had an error : {e}")

    try:
        bloc = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".storyItem__aaf871c1c5"))
        )
    except Exception as e:
        print(f"exception at part 2two::::  {e}")

    counter = 0
    for i in bloc:
        title = i.find_element(By.CSS_SELECTOR, ".headline__3a97424275")
        descr = i.find_element(By.CSS_SELECTOR, ".summary__a759320e4a")
        dic[counter] = {title.text, descr.text}
        counter += 1

    driver.quit()

    save(dic)


def save(new_data):
    analyze.az.sendtoQueue(new_data)
    last_data = load()
    if new_data:
        last_data["Data"].append(new_data)
        try:
            with open(os.path.join(DATA_PATH, "ScBloomberg.json"), "w", encoding="utf-8") as s:
                json.dump(last_data, s, ensure_ascii=False, indent=4)
            print("bloomberg done successfully")
        except:
            print("bloomberg: file failed at saving")
            print("bloomberg faled")
    else:
        print('bloomberg: data is empty, saving canceled')
        print("bloomberg failed")


def load(filename="ScBloomberg.json"):
    try:
        with open(os.path.join(DATA_PATH, "ScBloomberg.json"), "r", encoding="utf-8") as l:
            data = json.load(l)
        return (data)
    except:
        print(
            f"bloomberg : ScBloomberg.json is not where it sould be at {DATA_PATH}")
