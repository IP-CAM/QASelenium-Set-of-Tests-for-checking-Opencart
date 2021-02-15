from pages.BasePage import BasePage
from pages.locators.CategoryPageLocators import CategoryPageLocators as locator


class CategoryPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        super(CategoryPage, self).__init__(driver, base_url)

    def get_header_category(self):
        return self._get_element(locator.HEADER_CATEGORY)

    def get_description_category(self):
        return self._get_element(locator.DESCRIPTION_CATEGORY)

    def get_items_in_category(self):
        return self._get_elements(locator.ITEMS_IN_CATEGORY)

    def get_text_of_showing_block(self):
        return self._get_element_text(locator.SHOWING_ITEMS_ON_PAGE)