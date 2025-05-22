import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Start Browser session
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://practice.expandtesting.com/inputs")

# Enter/Type Number
test_number = "123456"
input_number = driver.find_element(by=By.ID, value="input-number")
input_number.send_keys(test_number)

# Enter/Type Text
test_text = "abcd"
input_text = driver.find_element(by=By.ID, value="input-text")
input_text.send_keys("hello")

# Enter/Type Password

# Enter/Type Date


# Display button
display_button = driver.find_element(by=By.ID, value="btn-display-inputs")
display_button.click()

# Verify number
output_number = driver.find_element(by=By.ID, value="output-number")
display_number = output_number.text

if test_number == display_number:
    print("Input Number verified.")
else:
    print("Output number and input number mismatch.Display number is: ", display_number)


# Verify text
time.sleep(10)
try:
    output_text = driver.find_element(by=By.ID, value="output-text")

    try:
        display_text = output_text.text
        assert display_text == test_text
        print("Text Assertion Passed.")
    except AssertionError:
        print("Assertion Failed. Input and Output text Mismatch.")
    except Exception as e:
        print(f"Error Occurred: {e}")

except Exception as e:
    print(f"Text field did not found.Exception: {e}")



print("Test Complete")

# Verify Password

# Verify Date

driver.quit()

