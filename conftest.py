import pytest

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from pages.elements_page import ElementsPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


def change_browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError("Unrecognized browser {}".format(browser_name))
    return driver


@pytest.fixture(autouse=True, scope='session')
def browser(request):
    driver = change_browser(request)
    yield driver
    driver.quit()


@pytest.fixture
def home_page(browser):
    home_page_url = "https://demoqa.com/"
    home_page = HomePage(browser, home_page_url)
    home_page.open()
    return home_page


@pytest.fixture(scope="class")
def elements_page(browser):
    elements_page_url = "https://demoqa.com/elements"
    elements_page = ElementsPage(browser, elements_page_url)
    elements_page.open()
    return elements_page
