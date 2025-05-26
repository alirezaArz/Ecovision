from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
dic = {}
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox()

driver.get("https://www.bon-bast.com/")

time.sleep(3)
try:
	var = WebDriverWait(driver, 10).until(
		EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.active"))
	)
	temp = []
	for i in var:
		temp.append(i.text)

	var = temp[:]
except Exception as e:
	print(f"{e}")

#try:
#	var2 = WebDriverWait(driver, 10).until(
#		EC.presence_of_all_elements_located((By.CLASS_NAME, "same_val"))
#	)
#	temp = []
#	for i in var2:
#		temp.append(i.text)
#	
#	var2 = temp[:]
#except Exception as e:
#	print(f"2:: {e}")

#var2 = var2[6:]

for element in var:
	item = list(element.split(" "))
	naame = f"{item[0]} : {item[1]}"
	dic[naame] = { 'buy' :item[-1] , 'sell' :item[-2]}


for i in dic:
	print( f"{i}   :   {dic[i]["buy"]} , {dic[i]["sell"]}")


driver.quit()