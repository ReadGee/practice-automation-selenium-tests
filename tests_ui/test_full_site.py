import random
import pytest
from selenium.webdriver.support.select import Select
from base.base_test import BaseTest
from pages import JsDelays, MainPage, FormFields, Popups, SliderPage


class TestTestingFullSite(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_Page = MainPage(driver)
        self.js_Delays = JsDelays(driver)
        self.form_fields = FormFields(driver)
        self.popups = Popups(driver)
        self.slider_page = SliderPage(driver)

    def test_js_delays(self):
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
        result = self.form_fields.alert.text == "Message received!"
        self.form_fields.alert.accept()
        assert result

    def test_popups(self):
        test_errors = []
        self.main_Page.click_popups()

        self.popups.alert_button.click()
        test_errors.append(self.popups.alert.text == "Hi there, pal!")
        self.popups.alert.accept()

        self.popups.confirm_button.click()
        self.popups.alert.accept()
        test_errors.append(self.popups.confirm_text.get_text == "OK it is!")

        self.popups.confirm_button.click()
        self.popups.alert.dismiss()
        test_errors.append(self.popups.confirm_text.get_text == "Cancel it is!")

        self.popups.prompt_button.click()
        self.popups.alert.accept()
        test_errors.append(self.popups.prompt_text.get_text == "Fine, be that way...")

        self.popups.prompt_button.click()
        text_for_prompt_alert = self.get_valid_username
        self.popups.alert.send_keys(text_for_prompt_alert)
        self.popups.alert.accept()

        test_errors.append(text_for_prompt_alert in self.popups.prompt_text.get_text)
        assert False not in test_errors

    def test_slider(self):
        test_errors = []
        self.main_Page.click_slider()

        for i in range(random.randint(3, 10)):
            random_value = random.randint(0, 100)
            self.slider_page.slider.set_value(random_value)
            test_errors.append(self.slider_page.slider_text.wait_until_text_to_be_present_in_element(str(random_value), 5))

        assert False not in test_errors
