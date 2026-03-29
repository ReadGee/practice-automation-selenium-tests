from selenium.webdriver.common.alert import Alert
from utils.Enum_Base import By
from base.Elements import Button, Text
from base.base_page import BasePage
from conftest import driver


class Popups(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def alert_button(self):
        return Button(self.driver, By.ID, 'alert')

    @property
    def confirm_button(self):
        return Button(self.driver, By.ID, 'confirm')

    @property
    def prompt_button(self):
        return Button(self.driver, By.ID, 'prompt')

    @property
    def confirm_text(self):
        return Text(self.driver, By.ID, 'confirmResult')

    @property
    def prompt_text(self):
        return Text(self.driver, By.ID, 'promptResult')

    @property
    def alert(self):
        return Alert(self.driver)