def test_main_page(browser, base_url):
    browser.get(base_url)
    assert "Your Store" in browser.title
    browser.save_screenshot(f"{browser.name}.png")