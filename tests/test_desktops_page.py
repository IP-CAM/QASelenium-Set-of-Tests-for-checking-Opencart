import pytest
from helpers import get_displayed_unique_element


@pytest.fixture
def category_url(base_url):
    return f"{base_url}/index.php?route=product/category&path=20"


@pytest.fixture
def browser(browser, category_url):
    browser.get(category_url)
    return browser


def test_browser_title_is_desktops(category_url, browser):
    """
     проверка заголовка страницы Desktops
    """
    assert category_url == browser.current_url
    assert "Desktops" in browser.title


def test_text_of_header_is_desktops(browser):
    """
    проверка наличия заголовка Desktops в странице
    """
    h2_css = "#content > h2"
    h2 = get_displayed_unique_element(browser, h2_css)
    assert h2.text == "Desktops"


def test_left_menu_present(browser):
    """
    проверка отображения меню слева
    """
    column_left_css = "#column-left"
    menu_items_css = "a"
    menu = get_displayed_unique_element(browser, column_left_css)
    menu_items = menu.find_elements_by_css_selector(menu_items_css)
    assert len(menu_items) == 11


def test_text_description_is_present(browser):
    """
    проверка отображения описания блока
    """
    description_css = "#content > div:nth-child(2) > div.col-sm-10 > p"
    description = get_displayed_unique_element(browser, description_css)
    assert description.text == "Example of category description text"


def test_count_elements_in_main_block(browser):
    """
    проверка количества блоков в разделе Desktops
    """
    items = browser.find_elements_by_css_selector("#content > div:nth-child(7) > div")
    assert len(items) == 12

    count_of_showing_elements = browser.find_element_by_css_selector("#content > div:nth-child(8) > "
                                                                     "div.col-sm-6.text-right")
    assert count_of_showing_elements.text == "Showing 1 to 12 of 12 (1 Pages)"
