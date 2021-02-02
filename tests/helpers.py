from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def assert_displayed_unique_element(browser, xpath):
    assert WebDriverWait(browser, 10).until(
        EC.visibility_of_any_elements_located((By.XPATH, xpath))
    )
    elements = browser.find_elements_by_xpath(xpath)
    assert len(elements) == 1
