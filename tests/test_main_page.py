from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_browser_title(base_url, browser):
    """
     проверка заголовка главной страницы
    """
    browser.get(f"{base_url}")
    assert base_url + "/" == browser.current_url
    assert "Your Store" in browser.title


def test_is_main_carousel_present(base_url, browser):
    """
    проверка отображения главного баннера
    """
    browser.get(f"{base_url}")
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "common-home"))
    )


def test_count_elements_in_featured_row_equals_four(base_url, browser):
    """
    проверка количества блоков в главном баннере
    """
    browser.get(f"{base_url}")
    items = browser.find_elements_by_xpath("//*[@id='content']/div[2]/div")
    assert len(items) == 4


def test_is_second_carousel_present(base_url, browser):
    """
    проверка отображения баннера с логотипами
    """
    browser.get(f"{base_url}")
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "carousel0"))
    )


def test_text_of_header_is_featured(base_url, browser):
    """
    проверка наличия заголовка Featured
    """
    browser.get(f"{base_url}")
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
    assert browser.find_element_by_xpath("//*[@id='content']/h3").text == "Featured"
