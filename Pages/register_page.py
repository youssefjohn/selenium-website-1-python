import logging

from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from Pages.signin_page import SignInPage
from Pages.home_page import HomePage
from selenium.webdriver import ActionChains
from Utilities.utils import custom_logger
import time
import logging

class RegisterPage(BaseDriver):
    log = custom_logger(logLevel=logging.INFO)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@id='last_name']")
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Email Address']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    PASSWORD_CONFIRM_FIELD = (By.XPATH, "//input[@id='password_confirmation']")
    SIGNUP_BTN = (By.XPATH, "//input[@value='Sign Up']")
    DUPLICATE_EMAIL = (By.XPATH, "//span[contains(text(),'The email address you have entered is already regi')]")
    PASSWORDS_DONT_MATCH = (By.XPATH, "//span[contains(text(),'Passwords do not match.')]")
    FIRST_NAME_STRING = "Youssef"
    LAST_NAME_STRING = "Moustahib"





    def register_user(self, email, password, confirm_password):
        self.log.info("Beginning 'register_user' function")
        self.action = ActionChains(self.driver)
        self.HP = HomePage(driver=self.driver)
        self.SI = SignInPage(driver=self.driver)
        self.HP.click_signin_btn()
        self.SI.click_on_sign_up()
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(self.FIRST_NAME_STRING)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(self.LAST_NAME_STRING)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.PASSWORD_CONFIRM_FIELD).send_keys(confirm_password)
        self.action.move_to_element(self.driver.find_element(*self.SIGNUP_BTN)).click().perform()
        #self.driver.find_element(*self.SIGNUP_BTN).click()
        self.log.info("Ending 'register_user' function")


    def check_successful(self):
        try:
            time.sleep(5)
            email = self.random_email_generator()
            password = self.random_password_generator()
            self.register_user(email=email, password=password, confirm_password=password)
            user_icon = self.driver.find_element(*self.SI.USER_ACCOUNT_ICON)
        except NoSuchElementException:
            self.log.error("Sign up was: *** UNSUCCESSFUL ***")
            return False
        else:
            self.log.info("Sign Up was: Successful")
            return True


    def check_unsuccessful_duplicate_email(self, email, password, confirm_password):
        try:
            self.register_user(email, password, confirm_password)
            # Investigate why the duplicate message only appears 70% of the time
            element = self.wait_for_presence_of_element(*self.DUPLICATE_EMAIL)
        except NoSuchElementException:
            self.log.error("Duplicate email message displaying: *** NO ***")
            return False
        else:
            self.log.info("Duplicate email message displaying: Yes")
            return True


    def check_passwords_dont_match(self):
        try:
            email = self.random_email_generator()
            password1 = self.random_password_generator(10)
            password2 = self.random_password_generator(11)
            self.register_user(email, password1, password2)
            element = self.driver.find_element(*self.PASSWORDS_DONT_MATCH)
        except NoSuchElementException:

            self.log.error("Password not matching message displaying:  *** NO ***")
            return False
        else:
            self.log.info("Password not matching message displaying: Yes")
            return True








