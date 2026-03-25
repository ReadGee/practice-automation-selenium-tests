from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, timeout: int = 10, open_page: bool = False, url: str = ''):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        if open_page:
            self.url = url
            self.open(url)

    def open(self, url: str=None):
        if url is None:
            self.driver.get(self.url)
        else:
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