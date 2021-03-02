import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"],
                     help="browser", required=True)
    parser.addoption("--bversion", action="store", help="version of browser")


@pytest.fixture
def base_url():
    return "https://demo.opencart.com"


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    bversion = request.config.getoption("--bversion")

    driver = None

    def close_browser():
        if driver is not None:
            driver.quit()

    request.addfinalizer(close_browser)

    caps = {
        "browserName": browser,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    if bversion:
        caps["browserVersion"] = bversion

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub/",
        desired_capabilities=caps
    )

    driver.maximize_window()

    return driver
