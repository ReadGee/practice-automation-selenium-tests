from utils.EnumBy import By
from base.Elements import Button, Text
from base.BasePage import BasePage
from conftest import driver


class JsDelays(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.Text = Text(self.driver, By.ID, 'delay')

    def check_delay(self, text: str):
        return self.Text.wait_until_text_to_be_present_in_element(expected_text=text, timeout=11)

    @property
    def button_start(self):
        return Button(self.driver, By.ID, 'start')
