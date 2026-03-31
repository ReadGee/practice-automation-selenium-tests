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

    def close(self, handle: str = None):
        if handle:
            current_handle = self.get_current_handle
            self.switch_to_handle(handle)
            self.driver.close()
            self.switch_to_handle(current_handle)
        else:
            self.driver.close()
            self.switch_to_handle(self.get_first_handle)



    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def switch_to_handle(self, handle: str):
        self.driver.switch_to.window(handle)

    def switch_to_last_handle(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_first_handle(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    @property
    def get_handles(self):
        return self.driver.window_handles

    @property
    def get_last_handle(self):
        return self.driver.window_handles[-1]

    @property
    def get_first_handle(self):
        return self.driver.window_handles[0]

    @property
    def get_current_handle(self):
        return self.driver.current_window_handle

    @property
    def get_source_page(self):
        return self.driver.page_source

    @property
    def get_driver_url(self):
        return self.driver.current_url