from selenium.common import TimeoutException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.EnumBy import By


class BaseElement:
    def __init__(self, driver_or_element,
                 E_By: By = By.NONE,
                 locator: str = None,
                 web_element=None
                 ):

        if isinstance(driver_or_element, BaseElement):
            self.parent = driver_or_element.find(timeout=5)
            self.driver = driver_or_element.driver
        else:
            self.parent = None
            self.driver = driver_or_element

        self._web_element = web_element

        if E_By != E_By.NONE:
            self.locator = (E_By.by, E_By.locator.format(locator))
        elif locator is not None:
            self.locator = locator
        else:
            raise ValueError(
                "Необходимо передать один из локаторов (ID, CLASS_NAME, CSS_SELECTOR, LINK_TEXT, XPATH, NAME, TAG_NAME или PARTIAL_LINK_TEXT).")

    def _create_element_instance(self, web_element, element_class=None):
        """
            Создает экземпляр элемента с переданным web_element
        """
        element_class = element_class or self.__class__

        return element_class(
            self,
            locator=self.locator,
            web_element=web_element
        )

    def _get_search_context(self, parent: BaseElement | WebElement | tuple = None, timeout: int = 15):
        """Вспомогательный метод для определения контекста поиска."""
        parent = parent or self.parent
        if parent is None:
            return self.driver

        try:
            if isinstance(parent, BaseElement):
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(parent.locator)
                )
            if isinstance(parent, tuple):
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(parent)
                )
            return parent
        except TimeoutException:
            print(f"\nРодитель {parent} не найден за {timeout} сек.")
            return None

    def find(self, timeout: int = 15, parent: BaseElement | WebElement | tuple[By, str] = None) -> WebElement | None:
        """
        Данный метод используется для поиска элементов на странице или в родителе.
        :param timeout: Максимальное время ожидания (Поиска) в секундах. (по умолчанию: ``15``)
        :param parent: Ссылка на родителя в котором необходимо найти элементы. Принимает ``WebElement``, ``Locator``, а также элементы наследуемые от ``BaseElement``. (Default: ``None``)
        :return: ``WebElement``, но если сработает исключение, то ``None``.
        :raise: TimeoutException: Если за отведенное время ничего не нашлось. Возвращает None
        """

        if self._web_element:
            return self._web_element

        context = self._get_search_context(parent, timeout)
        if context is None:
            return None

        try:
            return WebDriverWait(context, timeout).until(
                EC.presence_of_element_located(self.locator)
            )
        except TimeoutException:
            print(f"\nЭлемент {self.locator} не найден за {timeout} сек.")
            return None

    def find_all(self, timeout: int = 15, as_objects: bool = True, parent: BaseElement | WebElement | tuple[By, str] = None) -> [WebElement] | [BaseElement] | None:
        """
        Поиск всех элементов с возможностью указать родителя.
        :param timeout: Максимальное время ожидания (Поиска) в секундах. (по умолчанию: ``15``)
        :param parent: Ссылка на родителя в котором необходимо найти элементы. Принимает ``WebElement``, ``Locator``, а также элементы наследуемые от ``BaseElement``. (по умолчанию: ``None``)
        :param as_objects: если ``True`` - возвращает список объектов класса (по умолчанию),
                       если ``False`` - возвращает список ``WebElement``.
        :return: Список объектов класса или ``WebElement``.
        """

        context = self._get_search_context(parent, timeout)
        if context is None:
            return None

        try:
            # Ждем появления хотя бы одного элемента
            WebDriverWait(context, timeout).until(EC.presence_of_all_elements_located(self.locator))
            elements = context.find_elements(*self.locator)

            if not as_objects:
                return elements

            return [self._create_element_instance(el) for el in elements]
        except TimeoutException:
            print(f"\nЭлементы {self.locator} не найдены за {timeout} сек.")
            return []

    def click(self):

        element = self.find()
        print(f"\nКлик на элемент: {self._debug_info_elements(element)}")

        try:
            # Авто-скролл силами драйвера
            _ = element.location_once_scrolled_into_view
            element.click()
            return
        except (ElementClickInterceptedException, ElementNotInteractableException):
            print("Стандартный клик не удался, запуск ActionChains\n")

        try:
            ActionChains(self.driver).move_to_element(element).click().perform()
            return
        except Exception:
            print("ActionChains не удался, запуск способа через JavaScript\n")
            self.driver.execute_script("arguments[0].click();", element)

    def double_click(self):
        """Выполняет двойной клик на элементе"""
        element = self.find()
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def hover(self):
        element = self.find()
        print(f"\nНаведение на элемент: {self._debug_info_elements(element)}")

        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception:
            print(f"Не удалось навестись на элемент: {self._debug_info_elements(element)}")
            self.driver.execute_script("let evObj = document.createEvent('MouseEvents'); "
                                       "evObj.initMouseEvent('mouseover', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null); "
                                       "arguments[0].dispatchEvent(evObj);", element)

    def is_displayed(self, timeout: int = 5):
        element = self.find(timeout)
        if element != None:
            return element.is_displayed()
        else:
            return False

    def is_enabled(self):
        element = self.find()
        return element.is_enabled()

    def get_attribute(self, attr):
        element = self.find()
        return element.get_attribute(attr)

    def select(self):
        element = self.find()
        element.click()

    def is_checked(self, element=None):
        if type(element) is not WebElement:
            element = self.find()
        return element.get_attribute("checked") == 'true'

    @property
    def get_text(self):
        element = self.find()
        print(f"\nПолучен текст от элемента: {self._debug_info_elements(element)}")
        return element.text

    def wait_until_visible(self, timeout: int = 10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.locator)
            )

            if element:
                return True
            else:
                return False
        except TimeoutException:
            print(f'Элемент с локатором: {self.locator} не был найден в течение {timeout} секунд')
            return False

    def wait_until_clickable(self, timeout=10):
        """Ожидать, пока кнопка станет кликабельной."""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.locator))
            if element:
                return True
            else:
                return False
        except TimeoutException:
            print(f'Элемент с локатором: {self.locator} не стал кликабельным в течение {timeout} секунд')
            return False

    def wait_until_invisibility(self, timeout=10):
        """Ожидать, пока элемент исчезнет """
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            print(f"Элемент с локатором {self.locator} не исчез в течение {timeout} секунд")
            return False

    def wait_until_visible_all(self, timeout=10):
        """Ожидать, прогрузятся все элементы """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(self.locator))
            return True
        except TimeoutException:
            print(f"Элемент с локатором {self.locator} не прогрузился в течение {timeout} секунд")
            return False

    def wait_until_text_to_be_present_in_element(self, expected_text, timeout=10):
        """Ожидать, текст в элементе """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(self.locator, expected_text)
            )
            return True
        except TimeoutException:
            print(f"Элемент с локатором {self.locator} не прогрузился в течение {timeout} секунд")
            return False

    def wait_for_attribute(self, attribute, value, timeout=10):
        """Универсальное ожидание атрибута"""

        def condition(driver):
            return self.get_attribute(attribute) == value

        WebDriverWait(self.driver, timeout).until(condition)

    def send_keys(self, value: str):
        element = self.find()
        element.send_keys(value)

    @staticmethod
    def _debug_info_elements(element: WebElement) -> str:
        return f"Id: {element.id}, Location: {element.location}, Size: {element.size}, Text: {element.text}, Tag_Name: {element.tag_name}, Parent: {element.parent}"

