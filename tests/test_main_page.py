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
    main_banner_css = "#slideshow0 > div > div.swiper-slide.text-center.swiper-slide-active > img"
    banner_image = get_displayed_unique_element(browser, main_banner_css)
    banner_image.get_attribute('src').endswith('.jpg')


def test_count_elements_in_featured_row_equals_four(browser):
    """
    проверка количества блоков в главном баннере
    """
    items = browser.find_elements_by_css_selector("#slideshow0 > div > div")
    assert len(items) == 4


def test_is_second_carousel_items(browser):
    """
    проверка отображения баннера с логотипами
    """
    second_banner_css = "#carousel0"
    second_banner = browser.find_element_by_css_selector(second_banner_css)
    second_banner.is_displayed()


def test_text_of_header_is_featured(browser):
    """
    проверка наличия заголовка Featured
    """
    h3_css = "#content > h3"
    h3 = get_displayed_unique_element(browser, h3_css)
    assert h3.text == "Featured"
