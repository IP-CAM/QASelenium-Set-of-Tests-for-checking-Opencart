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
    header_new_customer_xpath = "//*[@id='content']/div/div[1]/div/h2"
    get_displayed_unique_element(browser, header_new_customer_xpath)

    header_new_customer = browser.find_element_by_xpath(header_new_customer_xpath)
    assert header_new_customer.text == "New Customer"


def test_header_of_block_returning_customer(browser):
    """
    проверка наличия заголовка в блоке Returning Customer
    """
    header_returning_customer_xpath = "//*[@id='content']/div/div[2]/div/h2"
    get_displayed_unique_element(browser, header_returning_customer_xpath)

    header_returning_customer = browser.find_element_by_xpath(header_returning_customer_xpath)
    assert header_returning_customer.text == "Returning Customer"


def test_button_continue_displayed_in_block_new_customer(browser):
    block_new_customer_xpath = "//*[@id='content']/div/div[1]"
    button_continue_xpath = "./div/a"
    get_displayed_unique_element(browser, block_new_customer_xpath)

    block_new_customer = browser.find_element_by_xpath(block_new_customer_xpath)
    button_continue = block_new_customer.find_element_by_xpath(button_continue_xpath)

    assert button_continue.is_displayed()
    assert "Continue" == button_continue.text
    assert button_continue.get_attribute("href").endswith("register")


def test_inputs_are_displayed_in_block_returning_customer(browser):
    """проверка """
    block_returning_customer_xpath = "//*[@id='content']/div/div[2]"
    input_email_xpath = ".//*[@id='input-email']"
    input_password_xpath = ".//*[@id='input-password']"
    button_login_xpath = "./div/form/input"

    get_displayed_unique_element(browser, block_returning_customer_xpath)

    block_returning_customer = browser.find_element_by_xpath(block_returning_customer_xpath)
    input_email = block_returning_customer.find_element_by_xpath(input_email_xpath)
    input_password = block_returning_customer.find_element_by_xpath(input_password_xpath)
    button_login = block_returning_customer.find_element_by_xpath(button_login_xpath)

    assert input_email.is_displayed()
    assert input_password.is_displayed()
    assert button_login.is_displayed()

    assert input_email.get_attribute("placeholder") == "E-Mail Address"
    assert input_password.get_attribute("placeholder") == "Password"
    assert button_login.get_attribute("value") == "Login"
    assert button_login.get_attribute("type") == "submit"