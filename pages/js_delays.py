from selenium.webdriver.common.by import By
from base.base_page import BasePage
from conftest import driver


class JsDelays(BasePage):

    _button_start = (By.ID, 'start')
    _text_delay = (By.ID, 'delay')

    def __init__(self, driver, timeout: int = 15):
        super().__init__(driver, timeout)

    def click_start(self):
        self.click(self._button_start)

    def check_delay(self, text: str):
        return self.wait_change_text_in_element(self._text_delay, text)