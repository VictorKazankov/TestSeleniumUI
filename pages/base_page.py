from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url=None, timeout=30):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        assert "ToolsQA" in self.browser.title
        sleep(1)

    def get_element_present(self, how, what):
        try:
            element = WebDriverWait(self.browser, timeout=4).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return element

    def get_elements_present(self, how, what):
        try:
            elements = WebDriverWait(self.browser, timeout=4).until(EC.presence_of_all_elements_located((how, what)))
        except NoSuchElementException:
            return False
        return elements
