import pytest
from base.base_test import BaseTest
from pages.js_delays import JsDelays
from pages.mainPA_page import MainPA


class TestTestingFullSite(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_Page = MainPA(driver)
        self.js_Delays = JsDelays(driver)

    def test_js_delays(self, driver):
        self.main_Page.click_js_delays()
        self.js_Delays.button_start.click()
        assert self.js_Delays.check_delay("Liftoff!")