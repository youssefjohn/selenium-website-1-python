import logging

from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from Utilities.utils import custom_logger


class SignInPage(BaseDriver):
    log = custom_logger(logLevel=logging.INFO)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Email Address']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BTN = (By.XPATH, "//input[@value='Login']")
    FORGOT_PASSWORD_BTN = (By.XPATH, "//a[@href='/password/reset']")
    USER_ACCOUNT_ICON = (By.XPATH, "//img[@class='zl-navbar-rhs-img ']")
    SIGN_UP_BTN = (By.XPATH, "//a[contains(text(),'Sign Up')]")


    def click_on_sign_up(self):
        self.log.info("Clicking on Sign Up button")
        self.driver.find_element(*self.SIGN_UP_BTN).click()



    def login(self, email, password):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()


    def verify_login_result(self, email, password):
        try:
            self.login(email, password)
            user_icon = self.driver.find_element(*self.USER_ACCOUNT_ICON)
        except NoSuchElementException:
            self.log.error("*** Login was: UNSUCCESSFUL ***")
            return False
        else:
            self.log.info("Login Successful")
            return True





