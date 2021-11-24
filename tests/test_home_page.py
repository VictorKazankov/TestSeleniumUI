from pages.elements_page import ElementsPage


def test_displayed_all_cards(home_page):
    """
    Test check that all cards elements are displayed on home page
    :param home_page:
    :return:
    """
    correct_names_cards_list = ['Elements', 'Forms', 'Alerts, Frame & Windows', 'Widgets', 'Interactions', 'Book Store '
                                                                                                           'Application']
    current_names_cards = home_page.get_names_cards()
    home_page.check_name_cards(correct_names_cards_list, current_names_cards)


def test_opened_elements_card(home_page):
    """
    Check that element page can open from home page
    :param home_page:
    :return:
    """
    home_page.move_to_elements_page()
    elements_page = ElementsPage(home_page.browser)
    elements_page.is_displayed_text_element_header()
    elements_page.is_displayed_element_navigation_panel()
