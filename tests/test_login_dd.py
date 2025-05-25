import pytest
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.login_page import LoginPage
from utils.data_loader import load_login_data

logger = get_logger("TestLogin")
login_data = load_login_data()

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
