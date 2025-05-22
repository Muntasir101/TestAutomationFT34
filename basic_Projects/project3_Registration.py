user_name = input("Enter your name: ")
user_password = input("Enter your password: ")
user_repass = input("Confirm your password: ")


from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Start Browser session
driver = webdriver.Firefox()
driver.maximize_window()


#expected_msg = "Successfully registered, you can log in now."
#Username


driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/register")
try:
    username = driver.find_element(by=By.ID, value="username")
    try:
        username.send_keys(user_name)
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"username field did not found.Exception: {e}")

# Password
try:
    password = driver.find_element(by=By.ID, value="password")
    try:
        password.send_keys(user_password)
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"Password field did not found.Exception: {e}")

# confirm Password
try:
    password = driver.find_element(by=By.ID, value="confirmPassword")
    try:
        password.send_keys(user_repass)
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"Password field did not found.Exception: {e}")

# Login Button
try:
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
    try:
        login_button.click()
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"Login Button did not found.Exception: {e}")

# Verify Registration Successfully
try:
    flash =WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[role='alert']")
        )
    )
    print("Flash Message Found:", flash.text)

    assert flash.text == "Successfully registered, you can log in now."
    print("Successfully registered.")

except AssertionError:
    print("Registration Failed.")

except Exception as e:
    print(f"Error Occurred: {e}")

driver.quit()