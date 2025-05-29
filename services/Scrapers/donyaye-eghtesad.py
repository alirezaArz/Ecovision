from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--headless")
def func(inp_arg):
    driver = webdriver.Firefox()
    driver.get("https://donya-e-eqtesad.com/newsstudios/search")


    try:
        var = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.NAME, 'query'))
        )
        var.click()
        var.send_keys(str(inp_arg))
        var.send_keys(Keys.RETURN)
    except Exception as e:
	    print(f"{e}")




func("ارز")