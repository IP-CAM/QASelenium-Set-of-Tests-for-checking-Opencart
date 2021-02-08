import pytest
from helpers import get_displayed_unique_element


@pytest.fixture
def customer_url(base_url):
    return f"{base_url}/index.php?route=account/login"


@pytest.fixture
def browser(browser, customer_url):
    browser.get(customer_url)
    return browser


def test_browser_title_is_account_login(customer_url, browser):
    """
     проверка заголовка страницы Account Login в браузере
    """
    assert customer_url == browser.current_url
    assert "Account Login" in browser.title


def test_header_of_block_new_customer(browser):
    """
    проверка наличия заголовка в блоке new customer
    """
    block_new_customer_css= "#content > div > div:nth-child(1) > div"
    header_new_customer_css = block_new_customer_css + " > h2"
    header_new_customer = get_displayed_unique_element(browser, header_new_customer_css)
    assert header_new_customer.text == "New Customer"


def test_header_of_block_returning_customer(browser):
    """
    проверка наличия заголовка в блоке Returning Customer
    """
    block_returning_customer_css = "#content > div > div:nth-child(2) > div"
    header_returning_customer_css = block_returning_customer_css + " > h2"
    header_returning_customer = get_displayed_unique_element(browser, header_returning_customer_css)
    assert header_returning_customer.text == "Returning Customer"


def test_button_continue_displayed_in_block_new_customer(browser):
    block_new_customer_css = "#content > div > div:nth-child(1) > div"
    button_continue_css = "a"

    block = get_displayed_unique_element(browser, block_new_customer_css)
    button_continue = block.find_element_by_css_selector(button_continue_css)

    assert button_continue.is_displayed()
    assert "Continue" == button_continue.text
    assert button_continue.get_attribute("href").endswith("register")


def test_inputs_are_displayed_in_block_returning_customer(browser):
    """проверка отображения полей имени и пароля клиента и кнопки авторизации"""
    block_returning_customer_css = "#content > div > div:nth-child(2) > div"
    input_email_css = "#input-email"
    input_password_css = "#input-password"
    button_login_css = "form > input"

    block = get_displayed_unique_element(browser, block_returning_customer_css)
    input_email = block.find_element_by_css_selector(input_email_css)
    input_password = block.find_element_by_css_selector(input_password_css)
    button_login = block.find_element_by_css_selector(button_login_css)

    assert input_email.is_displayed()
    assert input_password.is_displayed()
    assert button_login.is_displayed()

    assert input_email.get_attribute("placeholder") == "E-Mail Address"
    assert input_password.get_attribute("placeholder") == "Password"
    assert button_login.get_attribute("value") == "Login"
    assert button_login.get_attribute("type") == "submit"