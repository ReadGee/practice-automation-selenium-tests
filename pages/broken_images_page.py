from utils.EnumBy import By
from base.Elements import Image, Other
from base.BasePage import BasePage
from conftest import driver


class BrokenImagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def _get_main(self):
        return Other(self.driver, By.ID, 'main')

    @property
    def get_images(self):
        return Image(self._get_main, By.TAG_NAME, 'img').find_all()