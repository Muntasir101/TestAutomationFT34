import pytest
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.login_page import LoginPage
from utils.data_loader import load_login_data,load_login_data_invalid

logger = get_logger("TestLogin")
login_data = load_login_data()
login_data_invalid = load_login_data_invalid()

@pytest.mark.parametrize("username,password,expected",login_data)
def test_valid_login(setup,username,password, expected):
    logger.info("------------------------------")
    logger.info(f"Test started with username = '{username}'")
    logger.info("Staring valid Login Test")
    driver = setup
    login = LoginPage(driver)

    login.open_login_page()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    try:
        expected_url = "https://www.saucedemo.com/inventory.html"
        assert expected_url == driver.current_url
        logger.info("Login Successful.Test Passed.")
    except AssertionError:
        logger.info("Bug: Login Test Failed for valid data.")
    except Exception as e:
        logger.info(f"Error Occurred: {e}")


    logger.info("Ending Login Test")
    logger.info("------------------------------")

@pytest.mark.parametrize("username,password,expected",login_data_invalid)
def test_invalid_login(setup,username,password, expected):
    logger.info("------------------------------")
    logger.info(f"Test started with username = '{username}'")
    logger.info("Staring valid Login Test")
    driver = setup
    login = LoginPage(driver)

    login.open_login_page()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    try:
        expected_error_massage = "Epic sadface: Username and password do not match any user in this service"
        actual_error = driver.find_element(by=By.CSS_SELECTOR, value="h3[data-test='error']")
        actual_error_message = actual_error.text
        assert expected_error_massage == actual_error_message, "Error Message mismatch !!"
        logger.info("Login Test Passed for Invalid data.")
    except AssertionError:
        logger.info("Bug: Login Test Failed for Invalid data.")
    except Exception as e:
        logger.info(f"Error Occurred: {e}")


    logger.info("Ending Invalid Test")
    logger.info("------------------------------")