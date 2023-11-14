import pytest
from Pages.register_page import RegisterPage


@pytest.mark.usefixtures("setup")
class TestRegisterPage:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.RP = RegisterPage(self.driver)

    # @pytest.mark.run(order=3)
    # def test_user_registration_successful(self):
    #     assert self.RP.check_successful()

    @pytest.mark.run(order=1)
    def test_duplicate_email_failure(self):
        assert self.RP.check_unsuccessful_duplicate_email(email="youssef_moustahib@hotmail.com",
                                                          password="Selenium123",
                                                          confirm_password="Selenium123")

    # @pytest.mark.run(order=2)
    # def test_passwords_not_matching(self):
    #     assert self.RP.check_passwords_dont_match()

