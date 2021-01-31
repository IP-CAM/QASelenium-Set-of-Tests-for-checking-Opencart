import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera", "edge", "yandex"],
                     help="browser", required=True)


@pytest.fixture
def base_url():
    return "http://" + os.environ.get("LOCAL_IP")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    def close_browser():
        if driver is not None:
            driver.close()

    request.addfinalizer(close_browser)

    if browser == "chrome":
        options = ChromeOptions()
        if headless: options.headless = True
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser == "opera":
        options = OperaOptions()
        if headless: options.headless = True
        driver = webdriver.Opera(executable_path="operadriver", options=options)

    elif browser == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(executable_path="msedgedriver")

    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        if headless: options.headless = True
        driver = webdriver.Chrome(executable_path="yandexdriver", options=options)

    if maximized:
        driver.maximize_window()

    return driver
