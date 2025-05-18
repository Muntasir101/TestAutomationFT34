from selenium import webdriver
from selenium.webdriver.common.by import By


# Start Browser session
driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://practice.expandtesting.com/inputs")

test_number = "123456"
input_number = driver.find_element(by=By.ID, value="input-number")
input_number.send_keys(test_number)

# Display button
display_button = driver.find_element(by=By.ID, value="btn-display-inputs")
display_button.click()

# Verify
output_number = driver.find_element(by=By.ID, value="output-number")
display_number = output_number.text

if test_number == display_number:
    print("Input Number verified.")
else:
    print("Output number and input number mismatch.Display number is: ", display_number)




