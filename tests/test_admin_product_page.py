import pytest
from helpers import assert_displayed_unique_element
import time


@pytest.fixture
def right_user():
    return "user", "bitnami"


@pytest.fixture
def admin_url(base_url):
    return f"{base_url}/admin/"


@pytest.fixture
def browser(browser, admin_url, right_user):
    browser.get(admin_url)
    field_username_xpath = "//*[@id='input-username']"
    field_password_xpath = "//*[@id='input-password']"
    button_xpath = "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button"
    menu_catalog_xpath = "//*[@id='menu-catalog']/a"
    menu_products_xpath = "//*[@id='collapse1']/li[2]/a"
    field_username = browser.find_element_by_xpath(field_username_xpath)
    field_password = browser.find_element_by_xpath(field_password_xpath)
    button = browser.find_element_by_xpath(button_xpath)
    user, password = right_user
    field_username.send_keys(user)
    field_password.send_keys(password)
    button.click()

    assert_displayed_unique_element(browser, menu_catalog_xpath)
    menu_catalog = browser.find_element_by_xpath(menu_catalog_xpath)
    menu_catalog.click()

    assert_displayed_unique_element(browser, menu_products_xpath)
    menu_products = browser.find_element_by_xpath(menu_products_xpath)
    menu_products.click()

    return browser


def test_table_with_product_is_displayed(browser):
    table_xpath = "//*[@id='form-product']/div/table"
    assert_displayed_unique_element(browser, table_xpath)


def test_count_of_column(browser):
    column_xpath = "//*[@id='form-product']/div/table/thead/tr/td"
    headers = browser.find_elements_by_xpath(column_xpath)
    assert len(headers) == 8


def test_count_column_of_products_table(browser):
    table_xpath = "//*[@id='form-product']/div/table"
    assert_displayed_unique_element(browser, table_xpath)
    table = browser.find_element_by_xpath(table_xpath)

    header_image_xpath = "./thead/tr/td[2]"
    header_image = table.find_element_by_xpath(header_image_xpath)
    assert "Image" in header_image.text

    header_product_name_xpath = "./thead/tr/td[3]/a"
    header_product_name = table.find_element_by_xpath(header_product_name_xpath)
    assert "Product Name" in header_product_name.text

    header_model_xpath = "./thead/tr/td[4]/a"
    header_model = table.find_element_by_xpath(header_model_xpath)
    assert "Model" in header_model.text

    header_price_xpath = "./thead/tr/td[5]/a"
    header_price = table.find_element_by_xpath(header_price_xpath)
    assert "Price" in header_price.text

    header_quantity_xpath = "./thead/tr/td[6]/a"
    header_quantity = table.find_element_by_xpath(header_quantity_xpath)
    assert "Quantity" in header_quantity.text

    header_status_xpath = "./thead/tr/td[7]/a"
    header_status = table.find_element_by_xpath(header_status_xpath)
    assert "Status" in header_status.text

    header_action_xpath = "./thead/tr/td[8]"
    header_action = table.find_element_by_xpath(header_action_xpath)
    assert "Action" in header_action.text