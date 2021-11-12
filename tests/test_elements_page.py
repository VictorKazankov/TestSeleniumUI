def test_submit_data_to_text_box_fields(elements_page):
    correct_value_data_fields = ['Ivan Ivanov', 'ivan_ivanov@gamil.com', 'Kiev Somova 14', 'Lviv']
    elements_page.move_to_text_box_tab()
    elements_page.fill_date_to_fields(correct_value_data_fields, elements_page.browser)
    elements_page.check_added_user_data(correct_value_data_fields)
