#Eghtesad news
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH= os.path.join(BASE_DIR , "scraped")

options = Options()
options.add_argument("--headless")



def main():
  dic = {}
  driver = webdriver.Firefox()
  driver.get("https://www.eghtesadnews.com/")


  time.sleep(3)
  try:
    div = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.content.webgardi-box'))
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
      EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".fnb.fn15.clr04.ng-binding"))
    )
  except Exception as e:
    print(f"esdn had an error at : {e}")
  
  for i in range(len(titles)):
    dic[i] = titles[i].text

  driver.quit()

  save(dic)


def save(data):
    if data:
      try:
        with open(os.path.join(DATA_PATH , "Eghtesad_news.json") , "w" , encoding="utf-8") as s:
            json.dump(data , s , ensure_ascii= False , indent=4)
        print("esdn done successfully")
      except:
            print("esdn: file failed at saving")
            print("esdn faled")
    else:
        print('esdn: data is empty, saving canceled')
        print("esdn failed")

def load(filename= "Eghtesad_news.json"):
    try:
        with open( os.path.join(DATA_PATH , "Eghtesat_news.json") , "r" , encoding="utf-8") as l:
            data = json.load(l)
        return(data)
    except:
      print(f"esdn : Eghtesat_news.json is not where it sould be at {DATA_PATH}")
