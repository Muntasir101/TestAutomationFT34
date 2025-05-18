from selenium import webdriver
from selenium.webdriver.common.by import By


# Start Browser session
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://practice.expandtesting.com/login")

#Username
try:
    username = driver.find_element(by=By.ID, value="username")
    try:
        username.send_keys("practice123")
    except Exception as e:
        print(f"Error Occurred: {e}")
except Exception as e:
    print(f"username field did not found.Exception: {e}")

# Password
try:
    password = driver.find_element(by=By.ID, value="password")
    try:
        password.send_keys("SuperSecretPassword!")
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

# Verify Login Successfully
try:
    expected_url = "https://practice.expandtesting.com/secure"
    assert expected_url == driver.current_url
    print("Login Successful.")
except AssertionError:
    print("Login Failed.")
except Exception as e:
    print(f"Error Occurred: {e}")

driver.quit()
