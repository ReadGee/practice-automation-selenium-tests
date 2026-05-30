import random
import pytest
from pyexpat.errors import messages
from selenium.webdriver.support.select import Select
from base.BaseTest import BaseTest
from pages import JsDelays, MainPage, FormFields, Popups, SliderPage, CalendarsPage, ModalPage, HoverPage, WindowOperationsPage, AdsPage, ClickEventsPage, SpinnersPage


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

        form_fields.name_input.send_keys(self.get_valid_username)
        form_fields.password_input.send_keys(self.get_valid_password)

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

        form_fields.email_input.send_keys(self.get_valid_email)
        form_fields.message_input.send_keys(self.get_random_text(128))

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

    def test_simple_modal(self):
        simple_modal = ModalPage(self.driver)
        self.main_Page.click_modals()
        simple_modal.simple_modal_button.click()
        assert simple_modal.simple_modal_text is not None

    def test_form_modal(self):
        form_modal = ModalPage(self.driver)
        name = self.get_valid_username
        email = self.get_valid_email
        message = self.get_random_text(50)
        self.main_Page.click_modals()
        form_modal.form_modal_button.click()

        form_modal.name_form_modal_input.send_keys(name)
        form_modal.email_form_modal_input.send_keys(email)
        form_modal.message_form_modal_input.send_keys(message)
        form_modal.submit_form_modal_button.click()

        all_texts = [obj.get_text for obj in form_modal.form_modal_text]
        required = [name, email, message]

        assert all(req in all_texts for req in required), \
            f"Не найдены элементы: {[r for r in required if r not in all_texts]}"

    def test_window_operations(self):
        window_operations_page = WindowOperationsPage(self.driver)
        self.main_Page.click_window_operations()
        test_errors = []
        original_url = window_operations_page.get_driver_url
        count_handle = len(window_operations_page.get_handles)

        window_operations_page.new_tab_button[0].click()
        test_errors.append(len(window_operations_page.get_handles) > count_handle)
        window_operations_page.close(window_operations_page.get_last_handle)

        window_operations_page.new_tab_button[1].click()
        test_errors.append(original_url is not window_operations_page.get_driver_url)
        window_operations_page.back()

        window_operations_page.new_tab_button[2].click()
        test_errors.append(len(window_operations_page.get_handles) > count_handle)
        window_operations_page.close(window_operations_page.get_last_handle)

        assert False not in test_errors

    def test_hover(self):
        hover_page = HoverPage(self.driver)
        self.main_Page.click_hover()

        hover_page.hover_text.hover()

        assert hover_page.hover_text.get_text == "You did it!"

    def test_ads(self):
        ads_page = AdsPage(self.driver)
        self.main_Page.click_ads()

        result = ads_page.ads_modal.wait_until_visible(timeout=6)
        ads_page.close_modal_button.click()

        assert result

    @pytest.mark.parametrize("button_name, expected_text", [
        ("cat_button", "Meow!"),
        ("dog_button", "Woof!"),
        ("pig_button", "Oink!"),
        ("cow_button", "Moo!")
    ])
    def test_click_events(self, button_name, expected_text):
        self.main_Page.click_events()
        click_events_page = ClickEventsPage(self.driver)

        button = getattr(click_events_page, button_name)
        button.click()

        assert click_events_page.get_result_text == expected_text

    def test_spinners(self):
        self.main_Page.click_spinners()
        spinners_page = SpinnersPage(self.driver)

        assert spinners_page.get_spinner.wait_until_invisibility(15)