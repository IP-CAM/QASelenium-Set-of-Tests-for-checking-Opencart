import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def base_url(base_url):
    return f"{base_url}/index.php?route=product/product&path=57&product_id=49"


def test_browser_title_of_product(base_url, browser):
    """
     проверка заголовка браузера на странице продукта
    """
    browser.get(f"{base_url}")
    assert base_url == browser.current_url
    assert "Samsung Galaxy Tab 10.1" in browser.title


def test_header_of_page(base_url, browser):
    """
    проверка отображения заголовка товара в странице продукта
    """
    browser.get(f"{base_url}")
    header_of_product_xpath = "//*[@id='content']/div/div[2]/h1"
    header_of_product = browser.find_element_by_xpath(header_of_product_xpath)
    assert header_of_product.text == "Samsung Galaxy Tab 10.1"


@pytest.mark.parametrize("name, idx", [("Product Code:", 0), ("Reward Points:", 1), ("Availability:", 2)])
def test_features_of_product(base_url, browser, name, idx):
    """
    проверка кода, премии, доступного количества продукта
    """
    browser.get(f"{base_url}")
    features_of_product_xpath = "//*[@id='content']/div/div[2]/ul[1]/li"
    features_of_product = browser.find_elements_by_xpath(features_of_product_xpath)
    assert len(features_of_product) == 3
    assert name in features_of_product[idx].text


def test_main_image_of_product_is_present(base_url, browser):
    """
    проверка отображения изображения продукта
    """
    browser.get(f"{base_url}")
    main_img_xpath = "//*[@id='content']/div/div[1]/ul[1]/li[1]/a/img"
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, main_img_xpath))
    )
    main_img = browser.find_element_by_xpath(main_img_xpath)
    assert main_img.get_attribute("src").endswith(".jpg")


def test_price_of_product(base_url, browser):
    """
    проверка цены продукта на валюту и минус
    """
    browser.get(f"{base_url}")
    price_xpath = "//*[@id='content']/div/div[2]/ul[2]/li[1]/h2"
    currency_xpath = "//*[@id='form-currency']/div/button/strong"

    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, currency_xpath))
    )

    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, price_xpath))
    )
    currency = browser.find_element_by_xpath(currency_xpath)
    price = browser.find_element_by_xpath(price_xpath)

    assert currency.text in price.text
    float_price = float(price.text.lstrip("$"))
    assert float_price > 0
