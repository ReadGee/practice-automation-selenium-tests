from utils.Enum_Base import By
from base.Elements import Text
from base.base_page import BasePage
from conftest import driver


class HoverPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def hover_text(self):
        return Text(self.driver, By.ID, 'mouse_over')