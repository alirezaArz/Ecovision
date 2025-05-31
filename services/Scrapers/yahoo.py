from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--headless")


def main():
	dic = {}	
	driver = webdriver.Firefox()
	driver.get("https://finance.yahoo.com/")

	time.sleep(3)
	try:
		var = WebDriverWait(driver, 10).until(
			EC.presence_of_all_elements_located((By.TAG_NAME, "h3"))
		)
	except Exception as e:
		print(f"{e}")

	for i in range(len(var)):
		dic[i] = var[i]

	driver.quit()
	return (dic)
