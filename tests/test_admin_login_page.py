import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    проверка наличия заголовка с текстом о вводе логина и пароля
    """
    header_admin_login_xpath = "//*[@id='content']/div/div/div/div/div[1]/h1"
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, header_admin_login_xpath))
    )
    assert browser.find_element_by_xpath(header_admin_login_xpath).text == "Please enter your login details."


def test_field_username_is_present(browser):
    """проверка наличия поля ввода имени пользователя"""
    field_username_xpath = "//*[@id='input-username']"
    field_username = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, field_username_xpath))
    )
    assert field_username.get_attribute("placeholder") == "Username"


def test_field_password_is_present(browser):
    """проверка наличия поля ввода пароля пользователя"""
    field_password_xpath = "//*[@id='input-password']"
    field_password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, field_password_xpath))
    )
    assert field_password.get_attribute("placeholder") == "Password"


def test_button_login_is_present(browser):
    """проверка наличия кнопки авторизации пользователя"""
    button_login_xpath = "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button"
    button_login = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, button_login_xpath))
    )
    assert button_login.text == "Login"