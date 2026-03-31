from utils.EnumBy import By
from base.Elements import Button
from base.BasePage import BasePage
from conftest import driver


class WindowOperationsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def new_tab_button(self):
        return Button(self.driver, By.CLASS_NAME, 'custom_btn.btn_hover').find_all()