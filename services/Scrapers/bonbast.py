from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from halo import Halo 
import sys
from selenium.webdriver.firefox.options import Options
import random
import time
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH= os.path.join(BASE_DIR , "scraped")


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

def main():
  spinner.start()
  driver = webdriver.Firefox()
  driver.get("https://www.bon-bast.com/")
  time.sleep(random.randint(5, 20))
  driver.implicitly_wait(5)
  memo = []
  
  try:
    var = WebDriverWait(driver, 10).until(
      EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.table-condensed"))
    )
    for item in var:
      memo.append((item.text))
  except Exception as e:
    print(f"{e}")
  driver.quit()
  
  change = []
  for num in 0,1:
    for item in (memo[num].split('\n')):
      change.append(item)
    change.remove('Code Currency Sell Buy')

  result = {}

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

  spinner.stop()
  save(result)



def save(data):
    with open(os.path.join(DATA_PATH , "Bonbast.json") , "w" , encoding="utf-8") as s:
        json.dump(data , s , ensure_ascii= False , indent=4)

def load(filename= "Bonbast.json"):
    if os.path.exists(filename):
        try :
            with open( os.path.join(DATA_PATH , "Bonbast.json") , "r" , encoding="usf-8") as l:
                data = json.load(l)
        except Exception as e :
            data= {}
    else :
        data = {}
        return(data)