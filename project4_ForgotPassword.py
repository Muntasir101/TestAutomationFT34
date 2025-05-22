# email = input("Enter your Email: ")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Browser session
driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/forgot-password")

try:
    user_email = driver.find_element(by=By.ID, value="email")
    email = "user1mail.com"
    try:
        user_email.send_keys(email)
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"username field did not found.Exception: {e}")



#  Retrieve password Button
try:
    retrieve_password_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
    #print("login button: ")
    #print(login_button)
    try:
        retrieve_password_button.click()
    except Exception as e:
         print(f"Error Occurred: {e}")
except Exception as e:
    print(f"Retrieve Password Button did not found.Exception: {e}")


# Verify
try:
    flash = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[role='alert']")
        )
    )
    assert flash.text == "An e-mail has been sent to you which explains how to reset your password."
    print("Flash Message Found:", flash.text)
except AssertionError:
    print("Assertion Error.")
except Exception as e:
     error_message = driver.find_element(by=By.CSS_SELECTOR, value=".ms-1.invalid-feedback")
     error_message_text = error_message.text
     print(error_message_text)


driver.quit()