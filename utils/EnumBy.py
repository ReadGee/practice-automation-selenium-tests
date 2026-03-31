from enum import Enum
from selenium.webdriver.common.by import By

class By(Enum):

    NONE = (None, None)
    ID = (By.ID, "{}")
    CLASS_NAME = (By.CLASS_NAME, "{}")
    CSS_SELECTOR = (By.CSS_SELECTOR, "{}")
    XPATH = (By.XPATH, "{}")
    NAME = (By.NAME, "{}")
    TAG_NAME = (By.TAG_NAME, "{}")
    PARTIAL_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "{}")
    LINK_TEXT = (By.LINK_TEXT, "{}")
    AUTOTEST_ID = (By.CSS_SELECTOR, '[autotest-id="{}"]')
    BUTTON_ID = (By.CSS_SELECTOR, '[buttonid="{}"]')
    INPUT_ID = (By.CSS_SELECTOR, '[inputid="{}"]')
    ROUTER_LINK = (By.CSS_SELECTOR, '[routerlink="{}"]')

    def __init__(self, by: By, locator: str):
        self.by = by
        self.locator = locator