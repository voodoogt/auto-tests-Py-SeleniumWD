from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id("book").click()

    in_put = browser.find_element_by_css_selector("[id=answer]")
    in_put.send_keys(calc(browser.find_element_by_id("input_value").text))

    button = browser.find_element_by_id("solve")
    button.click()



finally:
    time.sleep(10)
    browser.quit()