import pytest
from helpers import get_displayed_unique_element


@pytest.fixture
def admin_url(base_url):
    return f"{base_url}/admin/"


@pytest.fixture
def browser(browser, admin_url):
    browser.get(admin_url)
    return browser


def test_browser_title_is_administration(admin_url, browser):
    """
     проверка заголовка страницы Administration в браузере
    """
    assert admin_url == browser.current_url
    assert "Administration" in browser.title


def test_header_of_block_login(browser):
    """
    проверка отображения заголовка с текстом о вводе логина и пароля
    """
    header_admin_login_xpath = "//*[@id='content']/div/div/div/div/div[1]/h1"
    get_displayed_unique_element(browser, header_admin_login_xpath)

    header_admin_login = browser.find_element_by_xpath(header_admin_login_xpath)

    assert header_admin_login.text == "Please enter your login details."


def test_field_username_is_visible(browser):
    """проверка отображения поля ввода имени пользователя"""
    field_username_xpath = "//*[@id='input-username']"

    get_displayed_unique_element(browser, field_username_xpath)

    field_username = browser.find_element_by_xpath(field_username_xpath)

    assert field_username.get_attribute("placeholder") == "Username"


def test_field_password_is_visible(browser):
    """проверка отображения поля ввода пароля пользователя"""
    field_password_xpath = "//*[@id='input-password']"
    get_displayed_unique_element(browser, field_password_xpath)

    field_password = browser.find_element_by_xpath(field_password_xpath)

    assert field_password.get_attribute("placeholder") == "Password"


def test_button_login_is_visible(browser):
    """проверка отображения кнопки авторизации пользователя"""
    button_login_xpath = "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button"
    get_displayed_unique_element(browser, button_login_xpath)

    button_login = browser.find_element_by_xpath(button_login_xpath)

    assert button_login.text == "Login"