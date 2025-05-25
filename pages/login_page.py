from selenium.webdriver.common.by import By
from utils.logger import get_logger

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.logger =  get_logger(self.__class__.__name__)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open_login_page(self):
        self.logger.info("Opening Login Page")
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self,username):
        self.logger.info(f"Entering Username: {username}")
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self,password):
        self.logger.info(f"Entering Password: {password}")
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.logger.info("Clicking Login Button")
        self.driver.find_element(*self.login_button).click()