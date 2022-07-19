import unittest
import pytest
from Pages.practise_page import PractisePage

@pytest.mark.usefixtures("setup")
class TestPractisePage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.PP = PractisePage(driver=self.driver)
        self.PP.target_url()

    def test_radio_btns(self):
        assert self.PP.radio_checkbox_btn_selection(self.PP.BMW_RADIO_BTN, self.PP.BENZ_RADIO_BTN,
                                           self.PP.HONDA_RADIO_BTN)

    def test_dropdown(self):
        assert self.PP.dropdown_selection(self.PP.CAR_DROPDOWN)


    def test_checkbox(self):
        assert self.PP.radio_checkbox_btn_selection(self.PP.BMW_CHECKBOX, self.PP.BENZ_CHECKBOX,
                                                    self.PP.HONDA_CHECKBOX)

