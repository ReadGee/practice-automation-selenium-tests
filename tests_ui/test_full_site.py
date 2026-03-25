import random
import pytest
from selenium.webdriver.support.select import Select
from base.base_test import BaseTest
from pages.js_delays import JsDelays
from pages.main_page import MainPage
from pages.form_fields import Form_fields


class TestTestingFullSite(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_Page = MainPage(driver)
        self.js_Delays = JsDelays(driver)
        self.form_fields = Form_fields(driver)

    def test_js_delays(self, driver):
        self.main_Page.click_js_delays()
        self.js_Delays.button_start.click()
        assert self.js_Delays.check_delay("Liftoff!")

    def test_form_fields(self, driver):
        self.main_Page.click_form_fields()

        self.form_fields.name_input.send_file(self.get_valid_username)
        self.form_fields.password_input.send_file(self.get_valid_password)

        favorite_drink = self.form_fields.drink_checkbox
        for fav_drink in favorite_drink:
            random_number = random.randint(0, 1)
            if(random_number == 1):
                fav_drink.click()

        favorite_color = self.form_fields.color_radio
        favorite_color = random.choice(favorite_color)
        favorite_color.click()

        dropdown = Select(self.form_fields.automation_context_menu.find())
        dropdown.select_by_index(random.randint(0, len(dropdown.options)-1))

        self.form_fields.email_input.send_file(self.get_valid_email)
        self.form_fields.message_input.send_file(self.get_random_text(128))

        self.form_fields.submit_button.click()
        assert self.form_fields.alert.text == "Message received!"