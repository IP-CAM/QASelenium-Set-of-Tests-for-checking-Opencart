import pytest
from pages.CategoryPage import CategoryPage


@pytest.fixture
def desktops_url(base_url):
    return f"{base_url}/desktops"


@pytest.fixture
def desktops_page(browser, desktops_url):
    page = CategoryPage(browser, desktops_url)
    page.open()
    return page


def test_browser_title_is_desktops(desktops_page):
    """проверка заголовка страницы Desktops"""
    assert desktops_page.get_title() == "Desktops"


def test_text_of_header_of_category_page(desktops_page):
    """проверка наличия заголовка Desktops в странице"""
    assert desktops_page.get_header_category().text == "Desktops"


def test_text_description(desktops_page):
    """проверка отображения описания блока"""
    assert desktops_page.get_description_category().text == "Example of category description text"


def test_count_elements_in_category(desktops_page):
    """проверка количества блоков в разделе Desktops"""
    items = desktops_page.get_items_in_category()
    assert len(items) == 12
    assert desktops_page.get_text_of_showing_block() == "Showing 1 to 12 of 12 (1 Pages)"
