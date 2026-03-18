from selenium.webdriver.common.by import By
from base.base_page import BasePage
from conftest import driver, get_base_url


class MainPA(BasePage):

    _javascript_delays = (By.CSS_SELECTOR, 'a[href*="javascript-delays"]')
    _form_fields = (By.CSS_SELECTOR, 'a[href*="form-fields"]')
    _popups = (By.CSS_SELECTOR, 'a[href*="popups"]')
    _slider = (By.CSS_SELECTOR, 'a[href*="slider"]')
    _calendars = (By.CSS_SELECTOR, 'a[href*="calendars"]')
    _modals = (By.CSS_SELECTOR, 'a[href*="modals"]')
    _tables = (By.CSS_SELECTOR, 'a[href*="tables"]')
    _window_operations = (By.CSS_SELECTOR, 'a[href*="window-operations"]')
    _hover = (By.CSS_SELECTOR, 'a[href*="hover"]')
    _ads = (By.CSS_SELECTOR, 'a[href*="ads"]')
    _gestures = (By.CSS_SELECTOR, 'a[href*="gestures"]')
    _file_download = (By.CSS_SELECTOR, 'a[href*="file-download"]')
    _click_events = (By.CSS_SELECTOR, 'a[href*="click-events"]')
    _spinners = (By.CSS_SELECTOR, 'a[href*="spinners"]')
    _file_upload = (By.CSS_SELECTOR, 'a[href*="file-upload"]')
    _iframes = (By.CSS_SELECTOR, 'a[href*="iframes"]')
    _broken_images = (By.CSS_SELECTOR, 'a[href*="broken-images"]')
    _broken_links = (By.CSS_SELECTOR, 'a[href*="broken-links"]')
    _accordions = (By.CSS_SELECTOR, 'a[href*="accordions"]')


    def __init__(self, driver, timeout: int = 15, open_page: bool = True):
        super().__init__(driver, timeout, open_page, get_base_url())

    #region click methods

    def click_js_delays(self):
        self.click(self._javascript_delays)

    def click_form_fields(self):
        self.click(self._form_fields)

    def click_popups(self):
        self.click(self._popups)

    def click_slider(self):
        self.click(self._slider)

    def click_calendars(self):
        self.click(self._calendars)

    def click_modals(self):
        self.click(self._modals)

    def click_tables(self):
        self.click(self._tables)

    def click_window_operations(self):
        self.click(self._window_operations)

    def click_hover(self):
        self.click(self._hover)

    def click_ads(self):
        self.click(self._ads)

    def click_gestures(self):
        self.click(self._gestures)

    def click_file_download(self):
        self.click(self._file_download)

    def click_iframes(self):
        self.click(self._iframes)

    def click_broken_images(self):
        self.click(self._broken_images)

    def click_broken_links(self):
        self.click(self._broken_links)

    def click_accordions(self):
        self.click(self._accordions)

    def click_spinners(self):
        self.click(self._spinners)

    def click_file_upload(self):
        self.click(self._file_upload)

    #endregion