from pages.BasePage import BasePage
from pages.locators.MainPageLocators import MainPageLocators as locator


class MainPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        super(MainPage, self).__init__(driver, base_url)

    def get_images_of_main_banner(self):
        return self._get_elements(locator.IMAGES_IN_MAIN_SLIDER)

    def get_featured_items(self):
        return self._get_elements(locator.FEATURED_ITEMS)

    def get_brand_pagination_items(self):
        return self._get_elements(locator.BRAND_PAGINATION_ITEMS)

    def get_main_pagination_items(self):
        return self._get_elements(locator.MAIN_PAGINATION_ITEMS)
