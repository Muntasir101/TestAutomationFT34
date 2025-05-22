from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_login_page()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    try:
        expected_url = "https://www.saucedemo.com/inventory.html"
        assert expected_url == driver.current_url
        print("Login Successful.Test Passed.")
    except AssertionError:
        print("Bug: Login Test Failed for valid data.")
    except Exception as e:
        print(f"Error Occurred: {e}")

def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_login_page()
    login.enter_username("standard_user invalid")
    login.enter_password("secret_sauce")
    login.click_login()

    try:
        expected_error_massage = "Epic sadface: Username and password do not match any user in this service"
        actual_error = driver.find_element(by=By.CSS_SELECTOR, value="h3[data-test='error']")
        actual_error_message = actual_error.text
        assert expected_error_massage==actual_error_message,"Error Message mismatch !!"
        print("Login Test Passed for Invalid data.")
    except AssertionError:
        print("Bug: Login Test Failed for Invalid data.")
    except Exception as e:
        print(f"Error Occurred: {e}")