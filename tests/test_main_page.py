import pytest
from helpers import get_displayed_unique_element


@pytest.fixture
def browser(browser, base_url):
    browser.get(base_url)
    return browser


def test_browser_title(browser):
    """
     проверка заголовка главной страницы
    """
    assert "Your Store" in browser.title


def test_is_main_carousel_present(browser):
    """
    проверка отображения главного баннера
    """
    main_banner_xpath = "//*[@id='common-home']"
    get_displayed_unique_element(browser, main_banner_xpath)


def test_count_elements_in_featured_row_equals_four(browser):
    """
    проверка количества блоков в главном баннере
    """
    items = browser.find_elements_by_xpath("//*[@id='content']/div[2]/div")
    assert len(items) == 4


def test_is_second_carousel_present(browser):
    """
    проверка отображения баннера с логотипами
    """
    second_banner_xpath = "//*[@id='carousel0']"
    get_displayed_unique_element(browser, second_banner_xpath)


def test_text_of_header_is_featured(browser):
    """
    проверка наличия заголовка Featured
    """
    h3_xpath = "//*[@id='content']/h3"
    h3 = browser.find_element_by_xpath(h3_xpath)
    get_displayed_unique_element(browser, h3_xpath)
    assert h3.text == "Featured"
