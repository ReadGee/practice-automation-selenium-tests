from utils.Enum_Base import By

from base.Elements import Button
from base.base_page import BasePage
from conftest import driver, get_base_url


class MainPage(BasePage):

    def __init__(self, driver, open_page: bool = True):
        super().__init__(driver, open_page, get_base_url())

    #region click methods

    def click_js_delays(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="javascript-delays"]').click()

    def click_form_fields(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="form-fields"]').click()

    def click_popups(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="popups"]').click()

    def click_slider(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="slider"]').click()

    def click_calendars(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="calendars"]').click()

    def click_modals(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="modals"]').click()

    def click_tables(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="tables"]').click()

    def click_window_operations(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="window-operations"]').click()

    def click_hover(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="hover"]').click()

    def click_ads(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="ads"]').click()

    def click_gestures(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="gestures"]').click()

    def click_file_download(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="file-download"]').click()

    def click_iframes(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="iframes"]').click()

    def click_broken_images(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="broken-images"]').click()

    def click_broken_links(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="broken-links"]').click()

    def click_accordions(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="accordions"]').click()

    def click_spinners(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="spinners"]').click()

    def click_file_upload(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="file-upload"]').click()

    def click_events(self):
        Button(self.driver, By.CSS_SELECTOR, 'a[href*="click-events"]').click()

    #endregion