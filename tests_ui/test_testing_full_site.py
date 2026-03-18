from base.base_test import BaseTest
from pages.js_delays import JsDelays
from pages.mainPA_page import MainPA


class TestTestingFullSite(BaseTest):

    def test_js_delays(self, driver):
        mainpage = MainPA(driver)
        page = JsDelays(driver)
        mainpage.click_js_delays()
        page.click_start()
        assert page.check_delay("Liftoff!")