from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.window import WindowTypes
import time

from Base.base_driver import BaseDriver


class HomePage(BaseDriver):
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
        self.driver.find_element(*self.HOME_BTN).click()


    def click_logo_btn(self):
        self.driver.find_element(*self.LOGO).click()


    def click_all_courses_btn(self):
        self.driver.find_element(*self.ALL_COURSES_BTN).click()


    def click_support_btn(self):
        self.driver.find_element(*self.SUPPORT_BTN).click()


    def click_signin_btn(self):
        self.driver.find_element(*self.SIGNIN_BTN).click()


    def check_button_clickable(self, click_function, target_url):
        try:
            click_function()
        except:
            print("Button not clickable")
        else:
            if self.driver.current_url == target_url:
                return True
            else:
                return False


    def navigation_bar_top(self):
        try:
            self.driver.find_element(*self.LOGO)
            self.driver.find_element(*self.HOME_BTN)
            self.driver.find_element(*self.ALL_COURSES_BTN)
            self.driver.find_element(*self.SUPPORT_BTN)
            self.driver.find_element(*self.SIGNIN_BTN)
        except:
            print("Navigation items missing/issue")
        else:
            return True


    def occurrencess_checker(self, element, num_of_occurrences):
        try:
            self.page_scroll()
            length_of_courses = len(self.driver.find_elements(*element))
        except:
            print("Course list has items missing/issues")
        else:
            if length_of_courses == num_of_occurrences:
                return True
            else:
                return False












