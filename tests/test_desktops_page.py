import pytest
from helpers import assert_displayed_unique_element


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
    h2_xpath = "//*[@id='content']/h2"
    assert_displayed_unique_element(browser, h2_xpath)

    h2 = browser.find_element_by_xpath(h2_xpath)
    assert h2.text == "Desktops"


def test_left_menu_present(browser):
    """
    проверка отображения меню слева
    """
    column_left_xpath = "//*[@id='column-left']"
    assert_displayed_unique_element(browser, column_left_xpath)


def test_text_description_is_present(browser):
    """
    проверка отображения описания блока
    """
    description_xpath = "//*[@id='content']/div[1]/div[2]/p"
    assert_displayed_unique_element(browser, description_xpath)
    description = browser.find_element_by_xpath(description_xpath)
    assert description.text == "Example of category description text"


def test_count_elements_in_main_block_equals_twelve(browser):
    """
    проверка количества блоков в разделе Desktops
    """
    items = browser.find_elements_by_xpath("//*[@id='content']/div[4]/div")
    assert len(items) == 12

    count_of_showing_elements = browser.find_element_by_xpath("//*[@id='content']/div[5]/div[2]")
    assert count_of_showing_elements.text == "Showing 1 to 12 of 12 (1 Pages)"
