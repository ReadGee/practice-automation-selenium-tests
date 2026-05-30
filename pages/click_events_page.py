from utils.EnumBy import By
from base.Elements import Button, Text
from base.BasePage import BasePage
from conftest import driver


class ClickEventsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def pig_button(self):
        return Button(self.driver, By.ON_CLICK, 'pigSound()')

    @property
    def dog_button(self):
        return Button(self.driver, By.ON_CLICK, 'dogSound()')

    @property
    def cow_button(self):
        return Button(self.driver, By.ON_CLICK, 'cowSound()')

    @property
    def cat_button(self):
        return Button(self.driver, By.ON_CLICK, 'catSound()')

    @property
    def get_result_text(self):
        return Text(self.driver, By.ID, 'demo').get_text