from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, base_url):
    browser.get(base_url)
    assert "Your Store" in browser.title
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "cart"))
    )
    browser.save_screenshot(f"{browser.name}.png")
