from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import json
from datetime import datetime

options = Options()
options.add_argument("--headless")

NYTIMES_DATA_PATH = r"T:\JAVASCRIPT\VGAnalyzer\services\Scrapers\nytimesDATA"
if not os.path.exists(NYTIMES_DATA_PATH):
    os.makedirs(NYTIMES_DATA_PATH, exist_ok=True)

def main():
    dic = {}
    driver = webdriver.Firefox()
    driver.get("https://www.nytimes.com/section/business/economy")
    time.sleep(random.randint(5, 20))
    driver.implicitly_wait(5)
    
    titles_elements = []
    descript_elements = []

    try:
        titles_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.e15t083i0'))
        )
        descript_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-1pga48a.e15t083i1'))
        )
    except Exception as e:
        print(f"Error fetching elements: {e}")

    if titles_elements and descript_elements:
        current_time = datetime.now().isoformat()
        num_items = min(len(titles_elements), len(descript_elements))
        
        processed_data_list = []
        for i in range(num_items):
            item_data = {
                "id": i + 1,
                "title": titles_elements[i].text,
                "summary": descript_elements[i].text,
                "image": 'placeholder.svg',
                "category": 'news',
                "importance": 'medium',
                "date": current_time
            }
            processed_data_list.append(item_data)
        
        if processed_data_list:
            dic = {"newsData": processed_data_list}
            save_data(dic, "nytimes_main_data.json")
            
    driver.quit()
    return (dic)

def search(inp_arg):
    dic = {}
    driver = webdriver.Firefox()
    driver.get("https://www.nytimes.com/")
    time.sleep(random.randint(5, 20))
    driver.implicitly_wait(15)

    try:
        btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.css-tkwi90.e1iflr850'))
        )
    except Exception as e:
        print(f"personal exception--------------------{e}")
        driver.quit()
        return dic
        
    btn.click()
    
    time.sleep(1)
    try:
        inp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'query'))
        )
    except Exception as e:
        print(f"personal exception2--------------------{e}")
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
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-nsjm9t'))
        )
        
        paras = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-e5tzus'))
        )
    except Exception as e:
        print(f"personal exception3--------------------{e}")

    if titles and paras:
        num_results = min(len(titles), len(paras))
        temp_results = []
        for i in range(num_results):
            temp_results.append(titles[i].text + ",," + paras[i].text)
        if temp_results:
            dic = {"search_results": temp_results} 
    
    driver.quit()
    return(dic)

def save_data(list_of_news_articles, filename):
    filepath = os.path.join(NYTIMES_DATA_PATH, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(list_of_news_articles, file, indent=4, ensure_ascii=False)
        print(f"Data formatted for React API saved to {filepath}")
    except Exception as e:
        print(f"Error saving data for React API to {filepath}: {e}")
