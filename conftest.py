import pytest
import logging
import os

from selenium import webdriver

LOG_FILE = '../logs/selenium.log'

logging.basicConfig(level=logging.DEBUG,
                    filename=LOG_FILE,
                    format='%(asctime)s.%(msecs)03d | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"],
                     help="browser", required=True)
    parser.addoption("--bversion", action="store", help="version of browser")
    parser.addoption("--executor", action="store", help="address of executor", default="127.0.0.1")
    parser.addoption("--pexec", action="store", help="port of executor", default="4444")


@pytest.fixture(scope='session')
def rm_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("Logs removed")


@pytest.fixture
def base_url():
    return "https://demo.opencart.com"


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    bversion = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    pexec = request.config.getoption("--pexec")

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
        command_executor=f"http://{executor}:{pexec}/wd/hub/",
        desired_capabilities=caps
    )

    test_name = request.node.name

    logger = logging.getLogger(f'Logger_of_{browser}_{driver.capabilities["browserVersion"]}')

    def close_browser():
        if driver is not None:
            driver.quit()
            logger.info(f'browser for {test_name} closed')
        logger.info(f'test {test_name} ended')

    request.addfinalizer(close_browser)

    driver.maximize_window()

    logger.info(f'browser for {test_name} opened')
    return driver
