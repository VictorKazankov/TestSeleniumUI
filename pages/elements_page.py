import json

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# locators

MAIN_HEADER = (By.XPATH, "//div[@class='main-header']")
NAVIGATION_PANEL = (By.XPATH, "//div[@class='element-group']")
TEXT_BOX_TAB = (By.XPATH, "//li[@id='item-0']")

CHECK_BOX_TAB = (By.XPATH, "//li[@id='item-1']")
USER_FORM_FIELDS = (By.XPATH, "//form[@id='userForm']/div[@class='mt-2 row']/div[last()]/*")
SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
RESULT_DATA_USER_BORDER = (By.XPATH, "//div[@class='border col-md-12 col-sm-12']")
HOME_FOLDER_LABEL = (By.XPATH, "//label[@for='tree-node-home']")
HOME_FOLDER_TITLE = (By.XPATH, "//label[@for='tree-node-home']/span[@class='rct-title']")
EXPAND_TREE_LABEL = (By.XPATH, '//button[@aria-label="Toggle"]')
EXPAND_TREE_STATUS = (By.XPATH, '//button[@aria-label="Toggle"]/*[@class="rct-icon rct-icon-expand-close"]')
CHILD_TREE_LIST = (By.XPATH, '//button[@aria-label="Toggle"]/following::ol/li')
TREE_FIRST_LEVEL_ELEMENTS = (By.XPATH, '//button[@aria-label="Toggle"]/following::ol/li/span')

RADIO_BOX_TAB = (By.XPATH, "//li[@id='item-2']")
YES_BUTTON = (By.XPATH, '//input[@id="yesRadio"]/following-sibling::label')
NO_BUTTON_DISABLE = (By.XPATH,
                     '//input[@id="noRadio"]/following-sibling::label[@class="custom-control-label disabled"]')
IMPRESSIVE_BUTTON = (By.XPATH, '//input[@id="impressiveRadio"]/following-sibling::label')
YES_RESULT_TEXT = (By.XPATH, '//p[normalize-space(text())="You have selected"]/span[normalize-space(text())="Yes"]')
IMPRESSIVE_RESULT_TEXT = (By.XPATH,
                          '//p[normalize-space(text())="You have selected"]/span[normalize-space(text())="Impressive"]')


class ElementsPage(BasePage):
    def is_displayed_text_element_header(self):
        header_element = self.get_element_present(*MAIN_HEADER)
        assert header_element.text == 'Elements'

    def is_displayed_element_navigation_panel(self):
        navigation_panel = self.get_element_present(*NAVIGATION_PANEL)
        assert navigation_panel

    def move_to_text_box_tab(self):
        self.get_element_present(*TEXT_BOX_TAB).click()

    def move_to_check_box_tab(self):
        self.get_element_present(*CHECK_BOX_TAB).click()

    def move_to_radio_box_tab(self):
        self.get_element_present(*RADIO_BOX_TAB).click()


class TextBoxTab(ElementsPage):
    def check_all_fields_display(self, correct_fields):
        fields = self.get_elements_present(*USER_FORM_FIELDS)
        current_fields = [field.text for field in fields]
        assert current_fields == correct_fields

    def check_submit_button_display(self):
        assert self.get_element_present(*SUBMIT_BUTTON)

    def fill_date_to_fields(self, correct_value_data_fields, br):
        for field, value in zip(self.get_elements_present(*USER_FORM_FIELDS), correct_value_data_fields.values()):
            field.click()
            field.clear()
            field.send_keys(value)
        submit_button = self.get_element_present(*SUBMIT_BUTTON)
        br.execute_script("arguments[0].click();", submit_button)

    def check_added_user_data(self, correct_value_data_fields):
        result_border = self.get_element_present(*RESULT_DATA_USER_BORDER)
        result_text = result_border.text
        if [value for value in correct_value_data_fields.values()] == '':
            pass
        if correct_value_data_fields['Name'] == '':
            correct_result_text = f'Email:{correct_value_data_fields["Email"]}\n' \
                                  f'Current Address :{correct_value_data_fields["Current Address"]}\n' \
                                  f'Permananet Address :{correct_value_data_fields["Permananet Address"]}'
        elif correct_value_data_fields['Email'] == '':
            correct_result_text = f'Name:{correct_value_data_fields["Name"]}\n' \
                                  f'Current Address :{correct_value_data_fields["Current Address"]}\n' \
                                  f'Permananet Address :{correct_value_data_fields["Permananet Address"]}'
        elif correct_value_data_fields['Current Address'] == '':
            correct_result_text = f'Name:{correct_value_data_fields["Name"]}\n' \
                                  f'Email:{correct_value_data_fields["Email"]}\n' \
                                  f'Permananet Address :{correct_value_data_fields["Permananet Address"]}'
        elif correct_value_data_fields['Permananet Address'] == '':
            correct_result_text = f'Name:{correct_value_data_fields["Name"]}\n' \
                                  f'Email:{correct_value_data_fields["Email"]}\n' \
                                  f'Current Address :{correct_value_data_fields["Current Address"]}'
        else:
            correct_result_text = f'Name:{correct_value_data_fields["Name"]}\n' \
                                  f'Email:{correct_value_data_fields["Email"]}\n' \
                                  f'Current Address :{correct_value_data_fields["Current Address"]}\n' \
                                  f'Permananet Address :{correct_value_data_fields["Permananet Address"]}'
        assert result_text == correct_result_text


class CheckBoxTab(ElementsPage):

    def is_displayed_home_folder(self):
        assert self.get_element_present(*HOME_FOLDER_LABEL)

    def is_displayed_home_text(self):
        title_element = self.get_element_present(*HOME_FOLDER_TITLE)
        assert title_element.text == 'Home'

    def expand_folder_tree(self):
        if self.get_element_present(*EXPAND_TREE_STATUS):
            self.get_element_present(*EXPAND_TREE_LABEL).click()

    def check_count_and_title_folders_first_level(self):
        folder_elements = self.get_elements_present(*CHILD_TREE_LIST)
        assert len(folder_elements) == 3
        name_folders = [folder.text for folder in folder_elements]
        assert name_folders == ['Desktop', 'Documents', 'Downloads']


class RadioBoxTab(ElementsPage):
    def get_yes_button(self):
        yes_button_element = self.get_element_present(*YES_BUTTON)
        assert yes_button_element.text == 'Yes'
        return yes_button_element

    def check_no_button_inactive(self):
        no_button_element_inactive = self.get_element_present(*NO_BUTTON_DISABLE)
        assert no_button_element_inactive.text == 'No'
        return no_button_element_inactive

    def get_impressive_button(self):
        impressive_button_element = self.get_element_present(*IMPRESSIVE_BUTTON)
        assert impressive_button_element.text == 'Impressive'
        return impressive_button_element

    def check_yes_result_selected(self):
        assert self.get_element_present(*YES_RESULT_TEXT)

    def check_impressive_result_selected(self):
        assert self.get_element_present(*IMPRESSIVE_RESULT_TEXT)
