import random
import pytest
from selenium.webdriver.support.select import Select
from base.base_test import BaseTest
from pages import JsDelays, MainPage, FormFields, Popups, SliderPage, CalendarsPage


class TestTestingFullSite(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_Page = MainPage(driver)
        self.driver = driver

    def test_js_delays(self):
        js_Delays = JsDelays(self.driver)
        self.main_Page.click_js_delays()
        js_Delays.button_start.click()
        assert js_Delays.check_delay("Liftoff!")

    def test_form_fields(self):
        form_fields = FormFields(self.driver)
        self.main_Page.click_form_fields()

        form_fields.name_input.send_file(self.get_valid_username)
        form_fields.password_input.send_file(self.get_valid_password)

        favorite_drink = form_fields.drink_checkbox
        for fav_drink in favorite_drink:
            random_number = random.randint(0, 1)
            if(random_number == 1):
                fav_drink.click()

        favorite_color = form_fields.color_radio
        favorite_color = random.choice(favorite_color)
        favorite_color.click()

        dropdown = Select(form_fields.automation_context_menu.find())
        dropdown.select_by_index(random.randint(0, len(dropdown.options)-1))

        form_fields.email_input.send_file(self.get_valid_email)
        form_fields.message_input.send_file(self.get_random_text(128))

        form_fields.submit_button.click()
        result = form_fields.alert.text == "Message received!"
        form_fields.alert.accept()
        assert result

    def test_popups(self):
        test_errors = []
        popups = Popups(self.driver)
        self.main_Page.click_popups()

        popups.alert_button.click()
        test_errors.append(popups.alert.text == "Hi there, pal!")
        popups.alert.accept()

        popups.confirm_button.click()
        popups.alert.accept()
        test_errors.append(popups.confirm_text.get_text == "OK it is!")

        popups.confirm_button.click()
        popups.alert.dismiss()
        test_errors.append(popups.confirm_text.get_text == "Cancel it is!")

        popups.prompt_button.click()
        popups.alert.accept()
        test_errors.append(popups.prompt_text.get_text == "Fine, be that way...")

        popups.prompt_button.click()
        text_for_prompt_alert = self.get_valid_username
        popups.alert.send_keys(text_for_prompt_alert)
        popups.alert.accept()

        test_errors.append(text_for_prompt_alert in popups.prompt_text.get_text)
        assert False not in test_errors

    def test_slider(self):
        test_errors = []
        slider_page = SliderPage(self.driver)
        self.main_Page.click_slider()

        for i in range(random.randint(3, 10)):
            random_value = random.randint(0, 100)
            slider_page.slider.set_value(random_value)
            test_errors.append(slider_page.slider_text.wait_until_text_to_be_present_in_element(str(random_value), 5))

        assert False not in test_errors

    def test_calendars(self):
        calendar_page = CalendarsPage(self.driver)
        self.main_Page.click_calendars()
        calendar_page.text_input.click()
        dict_of_months = calendar_page.get_months
        random_data = calendar_page.get_random_date(2015, 2030)

        now_month = dict_of_months.get(calendar_page.month_button.get_text)
        now_year = int(calendar_page.year_button.get_text)

        count, direction = calendar_page.get_scroll_count(now_year, now_month, random_data.get("year"), random_data.get("month"))

        if direction != "Stay":
            if direction == "Right":
                calendar_page.skip_next_number_of_months(count)
            elif direction == "Left":
                calendar_page.skip_prev_number_of_months(count)

        for day in calendar_page.days_button:
            if "dp-edge-day" in day.get_attribute("class"):
                continue
            elif day.get_text == str(random_data.get("day")):
                day.click()
                break

        calendar_page.submit_button.click()

        assert calendar_page.data_text.get_text == f"{random_data.get('year')}-{random_data.get('month'):02d}-{random_data.get('day'):02d}"
