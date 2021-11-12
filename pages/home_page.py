from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# locators
ALL_CARDS = (By.XPATH, "//div[@class='category-cards']/*")
ELEMENTS_CARD = (By.XPATH, "//div[@class='category-cards']/div[1]")


class HomePage(BasePage):
    def get_names_cards(self):
        all_cards = self.get_elements_present(*ALL_CARDS)
        all_names_cards = [name.text for name in all_cards]
        return all_names_cards

    def move_to_elements_page(self):
        element_card = self.get_element_present(*ELEMENTS_CARD)
        self.browser.execute_script("arguments[0].click();", element_card)

    def check_name_cards(self, correct_names_cards_list, current_names_cards):
        assert current_names_cards == correct_names_cards_list
