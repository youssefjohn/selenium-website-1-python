from Base.base_driver import BaseDriver
from Utilities.utils import custom_logger
from selenium.webdriver.common.by import By
import logging


class HomePage(BaseDriver):
    log = custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # URLS
    HOME = "https://courses.letskodeit.com/"
    COURSES = "https://courses.letskodeit.com/courses"
    SUPPORT = "https://courses.letskodeit.com/support"

    # Locators
    LOGO = (By.XPATH, "//img[@class='img-fluid']")
    HOME_BTN = (By.XPATH, "//a[contains(text(), 'HOME')]")
    ALL_COURSES_BTN = (By.XPATH, "//a[contains(text(), 'ALL COURSES')]")
    SUPPORT_BTN = (By.XPATH, "//a[contains(text(), 'SUPPORT')]")
    SIGNIN_BTN = (By.XPATH, "//a[@href='/login']")
    COURSE_LIST = (By.XPATH, "//div[@id='course-list']/div")
    BOTTOM_TEXT_BOXES = (By.XPATH, "//div[@class='content-style block features padding-top-50 padding-bottom-50 parrot']"
                                   "//div[@class='row']/div")

    FIXED_NUM_OF_COURSES = 10
    FIXED_NUM_OF_BOXES = 3

    def click_home_btn(self):
        self.log.info("Clicking home button")
        self.driver.find_element(*self.HOME_BTN).click()


    def click_logo_btn(self):
        self.log.info("Clicking logo button")
        self.driver.find_element(*self.LOGO).click()


    def click_all_courses_btn(self):
        self.log.info("Clicking all courses button")
        self.driver.find_element(*self.ALL_COURSES_BTN).click()


    def click_support_btn(self):
        self.log.info("Clicking support button")
        self.driver.find_element(*self.SUPPORT_BTN).click()


    def click_signin_btn(self):
        self.log.info("Clicking sign in button")
        self.driver.find_element(*self.SIGNIN_BTN).click()


    def check_button_clickable(self, click_function, target_url):
        try:
            click_function()
        except:
            self.log.error("Button is clickable: *** UNSUCCESSFUL ***")
        else:
            if self.driver.current_url == target_url:
                self.log.info("Current URL is equal to Target URL")
                return True
            else:
                self.log.error("*** Current URL is not equal to Target URL ***")
                return False


    def navigation_bar_top(self):
        try:
            self.driver.find_element(*self.LOGO)
            self.driver.find_element(*self.HOME_BTN)
            self.driver.find_element(*self.ALL_COURSES_BTN)
            self.driver.find_element(*self.SUPPORT_BTN)
            self.driver.find_element(*self.SIGNIN_BTN)
        except:
            self.log.error("*** Navigation bar error. Potential missing elements? ***")
        else:
            self.log.info("Navigation menu contains all expected elements")
            return True


    def occurrencess_checker(self, element, num_of_occurrences):
        try:
            self.page_scroll()
            length_of_courses = len(self.driver.find_elements(*element))
        except:
            self.log.error("*** Course list has items missing/issues ***")
        else:
            if length_of_courses == num_of_occurrences:
                self.log.info("Number of expected displayed courses is correct")
                return True
            else:
                self.log.error("*** Number of courses displayed on website is more/less than expected ***")
                return False












