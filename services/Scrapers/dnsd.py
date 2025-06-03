# donyayae - eghtesaad
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
from halo import Halo 
import sys
import os 
import json



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH= os.path.join(BASE_DIR , "scraped")

options = Options()
options.add_argument("--headless")


spinner = Halo(text='', spinner={
    "interval": 80,
    "frames": [
      "[    ]",
      "[   =]",
      "[  ==]",
      "[ ===]",
      "[====]",
      "[=== ]",
      "[==  ]",
      "[=   ]"
    ]
  })

def search(inp_arg):
    spinner.start()
    dic = {}
    driver = webdriver.Firefox()
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
         print(f"error at part 2 of the code::: {e}")

    for i in range(len(titles)):
        dic[i] = titles[i].text
    spinner.stop()
    driver.quit()
    save(dic)



def main():
    spinner.start()
    dic = {}
    driver = webdriver.Firefox()
    driver.get("https://donya-e-eqtesad.com/%D8%A8%D8%AE%D8%B4-%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF-183")

    time.sleep(random.randint(5, 20))
    driver.implicitly_wait(5)
    
    try:
        paras = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.lead'))
        )
    except Exception as e:
        print(f"personal error at search--------------{e}")
    
    
    for i in range(len(paras)):
        dic[i] = paras[i].text
    spinner.stop()
    driver.quit()
    save(dic)


def save(data):
    with open(os.path.join(DATA_PATH , "Dnsd.json") , "w" , encoding="utf-8") as s:
        json.dump(data , s , ensure_ascii= False , indent=4)

def load(filename= "Dnsd.json"):
    with open( os.path.join(DATA_PATH , "Dnsd.json") , "r" , encoding="utf-8") as l:
        data = json.load(l)
    return(data)
