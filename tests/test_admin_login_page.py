import pytest
from pages.LoginPage import LoginPage


@pytest.fixture
def admin_url(browser, base_url):
    return base_url + "/admin/index.php?route=common/login"


@pytest.fixture
def loginpage(browser, admin_url):
    page = LoginPage(browser, admin_url)
    page.open()
    return page


def test_browser_title_is_administration(loginpage):
    """проверка заголовка страницы Administration в браузере"""
    assert "Administration" in loginpage.get_title()


def test_text_of_forms_header(loginpage):
    """проверка отображения заголовка с текстом о вводе логина и пароля"""
    header = loginpage.get_form_header()
    assert header.is_displayed()
    assert header.text == "Please enter your login details."


def test_field_username(loginpage):
    """проверка отображения поля ввода имени, пароля пользователя и кнопки авторизации"""
    field_username = loginpage.get_input_username()
    assert field_username.is_displayed()
    assert field_username.get_attribute("placeholder") == "Username"


def test_field_password(loginpage):
    """проверка отображения поля ввода пароля пользователя"""
    field_password = loginpage.get_input_password()
    assert field_password.is_displayed()
    assert field_password.get_attribute("placeholder") == "Password"


def test_button_login(loginpage):
    """проверка отображения кнопки авторизации пользователя"""
    button_login = loginpage.get_button_login()
    assert button_login.is_displayed()
    assert button_login.text == "Login"


def test_forgotten_password_link(loginpage):
    """проверка отображения ссылки восстановления пароля"""
    forgotten_password_link = loginpage.get_forgotten_password_link()
    assert forgotten_password_link.is_displayed()
    assert forgotten_password_link.text == "Forgotten Password"
