from utils.Enum_Base import By
from base.Elements import Button, Text
from base.base_page import BasePage
from conftest import driver


class JsDelays(BasePage):

    def __init__(self, driver, timeout: int = 15):
        super().__init__(driver, timeout)
        self.Text = Text(self.driver, By.ID, 'delay')

    def check_delay(self, text: str):
        return self.Text.wait_until_text_to_be_present_in_element(expected_text=text, timeout=11)

    @property
    def button_start(self):
        return Button(self.driver, By.ID, 'start')
