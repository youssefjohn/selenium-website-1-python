import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    homepage = "https://courses.letskodeit.com/"
    practisepage = "https://courses.letskodeit.com/practice"

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
        time.sleep(4)

    def random_password_generator(self, num=11):
        password = ''.join(random.choice(string.ascii_letters) for _ in range(num))
        return password

    def random_email_generator(self, num=15, email_second="@gmail.com"):
        email_first = ''.join(random.choice(string.ascii_lowercase) for _ in range(num))
        return email_first + email_second

    def wait_for_presence_of_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 60, 2)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element

    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 60, 2)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element