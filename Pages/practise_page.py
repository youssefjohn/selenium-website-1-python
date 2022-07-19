from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select


class PractisePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    BMW_RADIO_BTN = (By.XPATH, "//input[@id='bmwradio']")
    BENZ_RADIO_BTN = (By.XPATH, "//input[@id='benzradio']")
    HONDA_RADIO_BTN = (By.XPATH, "//input[@id='hondaradio']")
    CAR_DROPDOWN = (By.XPATH, "//select[@id='carselect']")
    BMW_CHECKBOX = (By.XPATH, "//input[@id='bmwcheck']")
    BENZ_CHECKBOX = (By.XPATH, "//input[@id='benzcheck']")
    HONDA_CHECKBOX = (By.XPATH, "//input[@id='hondacheck']")
    SWITCH_WINDOW_BTN = (By.XPATH, "//button[@id='openwindow']")
    # (By.XPATH, "")
    # (By.XPATH, "")
    # (By.XPATH, "")
    # (By.XPATH, "")


    def target_url(self):
        self.driver.get(self.practisepage)


    def radio_checkbox_btn_selection(self, *args):
        radio_list = [*args]
        condition = False
        for btn in radio_list:
            btn = self.driver.find_element(*btn)
            btn.click()
            if not btn.is_selected():
                condition = False
                break
            else:
                condition = True
        return condition


    def dropdown_selection(self, dropdown):
        element = self.driver.find_element(*dropdown)
        select = Select(element)
        length_of_select = len(select.options)
        try:
            for num in range(length_of_select):
                select.select_by_index(num)
        except NoSuchElementException:
            print("Element not found")
            return False
        else:
            return True









