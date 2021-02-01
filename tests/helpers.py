def assert_displayed_unique_element(browser, xpath):
    elements = browser.find_elements_by_xpath(xpath)
    assert len(elements) == 1
    element = elements[0]
    assert element.is_displayed()
