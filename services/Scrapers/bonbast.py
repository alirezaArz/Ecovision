from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from halo import Halo 
import sys
from selenium.webdriver.firefox.options import Options
import random
import time
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

def getcurrency():
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
	return result

print(getcurrency())