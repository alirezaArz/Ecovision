from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--headless")



def main():
	dic = {}
	driver = webdriver.Firefox()
	driver.get("https://www.nytimes.com/section/business/economy")


	time.sleep(3)
	try:
		var = WebDriverWait(driver, 10).until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.e15t083i0'))
		)

	except Exception as e:
		print(f"{e}")

	for i in range(len(var)):
		dic[i] = var[i].text
	driver.quit()
	
	return (dic)


def search(inp_arg):
    dic = {}
    driver = webdriver.Firefox()
    driver.get("https://www.nytimes.com/")
    
    time.sleep(3)
    try:
        btn = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, '.css-tkwi90.e1iflr850'))
		)
    except Exception as e:
        print(f"personal exception--------------------{e}")
		
    btn.click()
	
    time.sleep(1)
    try:
        inp = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.NAME, 'query'))
		)
    except Exception as e:
        print(f"personal exception2--------------------{e}")
    
    inp.click()
    inp.send_keys(f"{inp_arg}")
    inp.send_keys(Keys.RETURN)

    time.sleep(3)
    
    try:
            titles = WebDriverWait(driver, 10).until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-nsjm9t'))
            
		)
            
            paras = WebDriverWait(driver, 10).until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-e5tzus'))
        )
    except Exception as e:
          print(f"personal exception3--------------------{e}")

    if len(titles) != len(paras):
          print("yaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    else:
          for i in range(len(titles)):
                dic[i] = titles[i].text + ",," + paras[i].text
    
    return(dic)
