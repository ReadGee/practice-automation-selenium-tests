import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    return get_base_url


@pytest.fixture
def open_main_page(driver, base_url):
    driver.get(base_url)
    return driver


def get_base_url():
    return "https://practice-automation.com/"
