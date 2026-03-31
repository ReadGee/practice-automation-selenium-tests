from utils.EnumBy import By
from base.Elements import Button, Modal
from base.BasePage import BasePage
from conftest import driver


class AdsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def ads_modal(self):
        return Modal(self.driver, By.ID, 'popmake-1272')

    @property
    def close_modal_button(self):
        return Button(self.ads_modal, By.CLASS_NAME, 'pum-close.popmake-close')