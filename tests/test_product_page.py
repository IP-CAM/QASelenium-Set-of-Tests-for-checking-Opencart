import pytest
from helpers import get_displayed_unique_element


@pytest.fixture
def product_url(base_url):
    return f"{base_url}/index.php?route=product/product&path=57&product_id=49"


@pytest.fixture
def browser(product_url, browser):
    browser.get(product_url)
    return browser


def test_browser_title_of_product(product_url, browser):
    """
     проверка заголовка браузера на странице продукта
    """
    assert product_url == browser.current_url
    assert "Samsung Galaxy Tab 10.1" in browser.title


def test_header_of_page(browser):
    """
    проверка отображения заголовка товара в странице продукта
    """
    header_of_product_css = "#content > div > div.col-sm-4 > h1"
    header_of_product = get_displayed_unique_element(browser, header_of_product_css)
    assert header_of_product.text == "Samsung Galaxy Tab 10.1"


@pytest.mark.parametrize("name, idx", [("Product Code:", 0), ("Reward Points:", 1), ("Availability:", 2)])
def test_features_of_product(browser, name, idx):
    """
    проверка кода, премии, доступного количества продукта
    """
    features_of_product_css = "#content > div > div.col-sm-4 > ul:nth-child(3) > li"
    features_of_product = browser.find_elements_by_css_selector(features_of_product_css)
    assert name in features_of_product[idx].text


def test_main_image_of_product_is_present(browser):
    """
    проверка отображения изображения продукта
    """
    main_img_css = "#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a > img"
    main_img = get_displayed_unique_element(browser, main_img_css)
    assert main_img.get_attribute("src").endswith(".jpg")


def test_price_of_product(browser):
    """
    проверка цены продукта на валюту и минус
    """
    price_css = "#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2"
    currency_css = "#form-currency > div > button > strong"
    price = get_displayed_unique_element(browser, price_css)
    currency = get_displayed_unique_element(browser, currency_css)

    assert currency.text in price.text
    float_price = float(price.text.lstrip("$"))
    assert float_price > 0
