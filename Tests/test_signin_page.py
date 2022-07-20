import unittest
import pytest
from Pages.signin_page import SignInPage
from Pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestSignInPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.SIP = SignInPage(driver=self.driver)
        self.HP = HomePage(driver=self.driver)
        self.HP.click_signin_btn()


    @pytest.mark.run(order=2)
    def test_login_successful(self):
        assert self.SIP.verify_login_result("youssef_moustahib@hotmail.com", "Selenium123")

    @pytest.mark.run(order=1)
    def test_login_unsuccessful(self):
        assert not self.SIP.verify_login_result("youssef_moustahib@hotmail.com", "sdfsdjvsd")






