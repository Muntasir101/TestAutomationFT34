from selenium import webdriver
from selenium.webdriver.common.by import By


# Start Browser session
driver = webdriver.Firefox()

driver.implicitly_wait(10)

driver.get("https://practice.expandtesting.com/inputs")

current_page_title = driver.title
print(current_page_title)

# latest
input_number = driver.find_element(by=By.ID, value="input-number")
input_number.send_keys("123456")

#driver.close()
# driver.quit()

