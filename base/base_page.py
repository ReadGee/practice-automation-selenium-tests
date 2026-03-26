from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, open_page: bool = False, url: str = None):
        self.driver = driver
        if open_page:
            self.url = url
            self.open(url)

    def open(self, url: str = None):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    @property
    def get_source_page(self):
        return self.driver.page_source