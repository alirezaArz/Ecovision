from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get('https://www.bbc.com/business')

try:
    # استفاده از CSS SELECTOR برای پیدا کردن عنصری که هر دو کلاس را دارد
    var = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-464f550b-2.iEUdAz'))
    )
    print(var.text)
except Exception as e:
    print(f"عنصر مورد نظر پیدا نشد: {e}")
finally:
    driver.quit()