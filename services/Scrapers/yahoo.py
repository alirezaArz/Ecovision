from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH= os.path.join(BASE_DIR , "scraped")

options = Options()
options.add_argument("--headless")


def main():
  dic = {}  
  driver = webdriver.Firefox()
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
    print(f"{e}")

  titles = []
  for i in var:
     if len(i.text) > 20:
        titles.append(i)
  
  
  for i in range(len(titles)):
    dic[i] = titles[i].text

  driver.quit()
  save(dic)


def save(data):
    with open(os.path.join(DATA_PATH ,"Yahoo.json") , "w" , encoding="utf-8") as s:
        json.dump(data , s , ensure_ascii= False , indent=4)

def load(filename= "Yahoo.json"):
    if os.path.exists(filename):
        try :
            with open( os.path.join(DATA_PATH ,"Yahoo.json") , "r" , encoding="usf-8") as l:
                data = json.load(l)
        except Exception as e :
            data= {}
    else :
        data = {}
    
    return (data)