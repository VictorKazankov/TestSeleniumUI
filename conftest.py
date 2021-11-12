import pytest

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from pages.home_page import HomePage
from pages.elements_page import ElementsPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


def change_browser(request):
    browser_name = request.config.getoption("--browser")
    options = None
    if browser_name == "chrome":
        desired_capabilities = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        port = '4445'

    elif browser_name == "firefox":
        desired_capabilities = DesiredCapabilities.FIREFOX
        port = '4446'
    else:
        raise ValueError("Unrecognized browser {}".format(browser_name))
    driver = webdriver.Remote(command_executor=f"http://localhost:{port}/wd/hub",
                              desired_capabilities=desired_capabilities,
                              options=options)
    return driver


@pytest.fixture(scope="function")
def browser(request):
    browser = change_browser(request)
    yield browser
    browser.quit()


@pytest.fixture
def home_page(browser):
    home_page_url = "https://demoqa.com/"
    home_page = HomePage(browser, home_page_url)
    home_page.open()
    return home_page


@pytest.fixture
def elements_page(browser):
    elements_page_url = "https://demoqa.com/elements"
    elements_page = ElementsPage(browser, elements_page_url)
    elements_page.open()
    return elements_page
