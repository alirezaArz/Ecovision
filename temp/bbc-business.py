from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()


driver.get('https://www.bbc.com/business')

var = WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.ID, 'main-content'))
)

input_element = driver.find_element(By.ID, "main-content")

print(var.text)
driver.quit()

