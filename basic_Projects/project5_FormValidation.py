import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Start Browser session
driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/form-validation")

try:
    pickup_date = driver.find_element(by=By.NAME, value="pickupdate")
    try:
        today = date.today().strftime("%y-%m-%d")
        pickup_date.send_keys(today)
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"pickup_date field did not found.Exception: {e}")

try:
    payment_method = driver.find_element(by=By.ID, value="validationCustom04")
    try:
        select = Select(payment_method)
        select.select_by_value("cashondelivery")
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"payment_method field did not found.Exception: {e}")

time.sleep(10)