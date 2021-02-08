import pytest
from helpers import get_displayed_unique_element


@pytest.fixture
def admin_url(base_url):
    return f"{base_url}/admin/"


@pytest.fixture
def browser(browser, admin_url):
    browser.get(admin_url)
    return browser


@pytest.fixture
def right_user():
    return "user", "bitnami"


@pytest.fixture
def wrong_user():
    return "wrong", "wrong"


def test_correct_login(browser, right_user):
    field_username_xpath = "//*[@id='input-username']"
    field_password_xpath = "//*[@id='input-password']"
    button_xpath = "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button"
    logout_xpath = "//*[@id='header']/div/ul/li[2]/a/span"
    field_username = browser.find_element_by_xpath(field_username_xpath)
    field_password = browser.find_element_by_xpath(field_password_xpath)
    button = browser.find_element_by_xpath(button_xpath)
    user, password = right_user
    field_username.send_keys(user)
    field_password.send_keys(password)
    button.click()
    # get_displayed_unique_element(browser, logout_xpath)
    logout = browser.find_element_by_xpath(logout_xpath)
    assert "Logout" in logout.text
    assert "user_token" in browser.current_url


def test_incorrect_login(browser, wrong_user):
    notification_area_xpath = "//*[@id='content']/div/div/div/div/div[2]/div"
    field_password_xpath = "//*[@id='input-password']"
    field_username_xpath = "//*[@id='input-username']"

    button_xpath = "//*[@id='content']/div/div/div/div/div[2]/form/div[3]/button"

    field_username = browser.find_element_by_xpath(field_username_xpath)
    field_password = browser.find_element_by_xpath(field_password_xpath)
    button = browser.find_element_by_xpath(button_xpath)

    user, password = wrong_user
    field_username.send_keys(user)
    field_password.send_keys(password)
    button.click()
    get_displayed_unique_element(browser, notification_area_xpath)
    notification_area = browser.find_element_by_xpath(notification_area_xpath)
    assert "No match for Username and/or Password." in notification_area.text
    get_displayed_unique_element(browser, field_username_xpath)
    get_displayed_unique_element(browser, field_password_xpath)
    get_displayed_unique_element(browser, button_xpath)
    assert "user_token" not in browser.current_url
