import pytest
from pages.AccountLoginPage import AccountLoginPage


@pytest.fixture
def account_login_page(browser, base_url):
    url = base_url + '/index.php?route=account/login'
    page = AccountLoginPage(browser, url)
    page.open()
    return page


def test_browser_title_is_account_login(account_login_page):
    """проверка заголовка страницы Account Login в браузере"""
    assert "Account Login" in account_login_page.get_title()


def test_header_of_block_new_customer(account_login_page):
    """проверка наличия заголовка в блоке new customer"""
    assert account_login_page.get_text_header_of_block_new_customer() == "New Customer"


def test_header_of_block_returning_customer(account_login_page):
    """проверка наличия заголовка в блоке Returning Customer"""
    assert account_login_page.get_text_header_of_block_returned_customer() == "Returning Customer"


def test_button_continue_in_block_new_customer(account_login_page):
    button = account_login_page.get_button_continue()
    assert button.text == "Continue"
    assert button.get_attribute("href").endswith("register")


def test_inputs_in_block_returning_customer(account_login_page):
    """проверка полей имени и пароля клиента и кнопки авторизации"""
    input_email = account_login_page.get_field_username_of_returned_customer()
    input_password = account_login_page.get_field_password_of_returned_customer()
    button_login = account_login_page.get_button_login_of_returned_customer()

    assert input_email.get_attribute("placeholder") == "E-Mail Address"
    assert input_password.get_attribute("placeholder") == "Password"
    assert button_login.get_attribute("value") == "Login"
    assert button_login.get_attribute("type") == "submit"
