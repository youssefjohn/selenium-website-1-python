import pytest
import unittest
from Pages.home_page import HomePage



@pytest.mark.usefixtures("setup")
class TestHomePage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.TXOB = HomePage(driver=self.driver)

    @pytest.mark.run(order=1)
    def test_navigation_bar(self):
        assert self.TXOB.navigation_bar_top()

    @pytest.mark.run(order=2)
    def test_course_list(self):
        assert self.TXOB.occurrencess_checker(element=self.TXOB.COURSE_LIST, num_of_occurrences=self.TXOB.FIXED_NUM_OF_COURSES)

    @pytest.mark.run(order=3)
    def test_bottom_text_boxes(self):
        assert self.TXOB.occurrencess_checker(element=self.TXOB.BOTTOM_TEXT_BOXES, num_of_occurrences=self.TXOB.FIXED_NUM_OF_BOXES)

    @pytest.mark.run(order=4)
    def test_home_btn_clickable(self):
        assert self.TXOB.check_button_clickable(click_function=self.TXOB.click_home_btn,
                                                target_url=self.TXOB.HOME)

    @pytest.mark.run(order=5)
    def test_logo_btn_clickable(self):
        assert self.TXOB.check_button_clickable(click_function=self.TXOB.click_logo_btn,
                                                target_url=self.TXOB.HOME)

    @pytest.mark.run(order=6)
    def test_all_courses_btn_clickable(self):
        assert self.TXOB.check_button_clickable(click_function=self.TXOB.click_all_courses_btn,
                                                target_url=self.TXOB.COURSES)

    @pytest.mark.run(order=7)
    def test_support_btn_clickable(self):
        assert self.TXOB.check_button_clickable(click_function=self.TXOB.click_support_btn,
                                                target_url=self.TXOB.SUPPORT)