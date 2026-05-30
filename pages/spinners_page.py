from utils.EnumBy import By
from base.Elements import Spinner
from base.BasePage import BasePage
from conftest import driver


class SpinnersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def get_spinner(self):
        return Spinner(self.driver, By.CLASS_NAME, 'spinner-hidden')