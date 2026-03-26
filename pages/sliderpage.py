from utils.Enum_Base import By
from base.Elements import Text, Slider
from base.base_page import BasePage
from conftest import driver


class SliderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def slider(self):
        return Slider(self.driver, By.ID, 'slideMe')

    @property
    def slider_text(self):
        return Text(self.driver, By.ID, 'value')