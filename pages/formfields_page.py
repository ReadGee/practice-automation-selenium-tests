from selenium.webdriver.common.alert import Alert

from utils.EnumBy import By
from base.Elements import Button, Input, Checkbox, Radio, ContextMenu
from base.BasePage import BasePage
from conftest import driver


class FormFields(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def name_input(self):
        return Input(self.driver, By.ID, 'name-input')

    @property
    def password_input(self):
        return Input(self.driver, By.CSS_SELECTOR, 'input[type="password"]')

    @property
    def drink_checkbox(self):
        return Checkbox(self.driver, By.NAME, 'fav_drink').find_all()

    @property
    def color_radio(self):
        return Radio(self.driver, By.NAME, 'fav_color').find_all()

    @property
    def automation_context_menu(self):
        return ContextMenu(self.driver, By.ID, 'automation')

    @property
    def email_input(self):
        return Input(self.driver, By.ID, 'email')

    @property
    def message_input(self):
        return Input(self.driver, By.ID, 'message')

    @property
    def submit_button(self):
        return Button(self.driver, By.ID, 'submit-btn')

    @property
    def alert(self):
        return Alert(self.driver)