from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# locators

MAIN_HEADER = (By.XPATH, "//div[@class='main-header']")
NAVIGATION_PANEL = (By.XPATH, "//div[@class='element-group']")
TEXT_BOX_TAB = (By.XPATH, "//li[@id='item-0']")
USER_FORM_FIELDS = (By.XPATH, "//form[@id='userForm']/div[@class='mt-2 row']/div[last()]/*")
SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
RESULT_DATA_USER_BORDER = (By.XPATH, "//div[@class='border col-md-12 col-sm-12']")


class ElementsPage(BasePage):
    def is_displayed_text_element_header(self):
        header_element = self.get_element_present(*MAIN_HEADER)
        assert header_element.text == 'Elements'

    def is_displayed_element_navigation_panel(self):
        navigation_panel = self.get_element_present(*NAVIGATION_PANEL)
        assert navigation_panel

    def move_to_text_box_tab(self):
        self.get_element_present(*TEXT_BOX_TAB).click()

    def check_all_fields_display(self, correct_fields):
        fields = self.get_elements_present(*USER_FORM_FIELDS)
        current_fields = [field.text for field in fields]
        assert current_fields == correct_fields

    def check_submit_button_display(self):
        assert self.get_element_present(*SUBMIT_BUTTON)

    def fill_date_to_fields(self, correct_value_data_fields, br):
        for field, text in zip(self.get_elements_present(*USER_FORM_FIELDS), correct_value_data_fields):
            field.click()
            field.clear()
            field.send_keys(text)
        a = self.get_element_present(*SUBMIT_BUTTON)
        br.execute_script("arguments[0].click();", a)
        pass

    def check_added_user_data(self, correct_value_data_fields):
        result_border = self.get_element_present(*RESULT_DATA_USER_BORDER)
        result_text = result_border.text
        b = f'Name:{correct_value_data_fields[0]}\nEmail:{correct_value_data_fields[1]}\n' \
            f'Current Address :{correct_value_data_fields[2]}\nPermananet Address :{correct_value_data_fields[3]}'
        assert result_text == b
