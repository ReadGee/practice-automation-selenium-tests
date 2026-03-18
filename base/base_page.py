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

    # def find(self, locator):
    #     return self.wait.until(EC.visibility_of_element_located(locator))  """Legacy Code"""

    def find(self, locator: tuple[str, str], parent: WebElement=None):
        if parent:
            return self.wait.until(
                lambda d: parent.find_element(*locator)
            )
        return self.wait.until(
            ec.visibility_of_element_located(locator)
        )

    def finds(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def wait_change_text_in_element(self, locator: tuple[str, str], text: str):
        return self.wait.until(
            ec.text_to_be_present_in_element(locator, text)
        )

    def click(self, locator: tuple[str, str], parent: WebElement=None):
        self.find(locator, parent).click()

    def value(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    @property
    def get_source_page(self):
        return self.driver.page_source