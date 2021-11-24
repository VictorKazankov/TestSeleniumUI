import pytest

from pages.elements_page import CheckBoxTab, TextBoxTab, RadioBoxTab


class TestTextBoxTab:
    @pytest.fixture(scope="class")
    def text_box(self, elements_page):
        elements_page.move_to_text_box_tab()
        text_box = TextBoxTab(elements_page.browser)
        yield text_box

    testdata = [
        ("all fields", {'Name': 'Ivan Ivanov', 'Email': 'ivan_ivanov@gamil.com', 'Current Address': 'Kiev Somova 14',
                        'Permananet Address': 'Lviv'}),
        ("no Name field", {'Name': '', 'Email': 'ivan_ivanov@gamil.com', 'Current Address': 'Kiev Somova 14',
                           'Permananet Address': 'Lviv'}),
        ("no Email field", {'Name': 'Ivan Ivanov', 'Email': '', 'Current Address': 'Kiev Somova 14',
                            'Permananet Address': 'Lviv'}),
        ("no Current Address field", {'Name': 'Ivan Ivanov', 'Email': 'ivan_ivanov@gamil.com', 'Current Address': '',
                                      'Permananet Address': 'Lviv'}),
        ("no Permananet Address field",
         {'Name': 'Ivan Ivanov', 'Email': 'ivan_ivanov@gamil.com', 'Current Address': 'Kiev Somova 14',
          'Permananet Address': ''})
    ]

    @pytest.mark.parametrize(
        argnames=('name_test', 'field_values'), argvalues=testdata,
        ids=[i[0] for i in testdata]
    )
    def test_submit_data_to_text_box_fields(self, text_box, name_test, field_values):
        text_box.move_to_text_box_tab()
        text_box.fill_date_to_fields(field_values, text_box.browser)
        text_box.check_added_user_data(field_values)


class TestCheckBoxTab:
    @pytest.fixture(scope="class")
    def check_box(self, elements_page):
        elements_page.move_to_check_box_tab()
        check_box = CheckBoxTab(elements_page.browser)
        yield check_box

    def test_check_home_folder(self, check_box):
        check_box.is_displayed_home_folder()
        check_box.is_displayed_home_text()

    def test_check_plus_and_minus_signs(self, check_box):
        check_box.move_to_check_box_tab()

    def test_open_folder_tree(self, check_box):
        check_box.expand_folder_tree()
        check_box.check_count_and_title_folders_first_level()


class TestRadioButtonTab:
    @pytest.fixture(scope="class")
    def radio_box(self, elements_page):
        elements_page.move_to_radio_box_tab()
        radio_box = RadioBoxTab(elements_page.browser)
        yield radio_box

    def test_check_result_of_yes_selected(self, radio_box):
        yes_button = radio_box.get_yes_button()
        yes_button.click()
        radio_box.check_yes_result_selected()

    def test_check_result_of_impressive_selected(self, radio_box):
        impressive_button = radio_box.get_impressive_button()
        impressive_button.click()
        radio_box.check_impressive_result_selected()

    def test_check_no_button_inactive(self, radio_box):
        assert radio_box.check_no_button_inactive()
