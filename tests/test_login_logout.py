import pytest
from pages.LoginPage import LoginPage


@pytest.fixture
def login_page(browser, base_url):
    url = f"{base_url}/admin/"
    page = LoginPage(browser, url)
    page.open()
    return page


@pytest.fixture
def right_user():
    return "user", "bitnami"


@pytest.fixture
def wrong_user():
    return "wrong", "wrong"


def test_correct_login(login_page, right_user):
    user, password = right_user
    admin_page = login_page.login(user, password)
    assert admin_page.get_logout_link().text == "Logout"
    assert admin_page.get_profile().text == "John Doe"


def test_incorrect_login(login_page, wrong_user):
    user, password = wrong_user
    login_page.login(user, password)
    assert "No match for Username and/or Password." in login_page.get_notification().text
    assert login_page.get_input_username().is_displayed()
    assert login_page.get_input_password().is_displayed()
    assert login_page.get_button_login().is_displayed()
