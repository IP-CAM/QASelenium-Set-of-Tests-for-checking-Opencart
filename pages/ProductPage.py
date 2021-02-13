from pages.BasePage import BasePage
from pages.locators.ProductPageLocators import ProductPageLocators as locator


class ProductPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        super(ProductPage, self).__init__(self.driver,
                                          self.url)

    def get_text_header_product(self):
        return self._get_element_text(locator.HEADER_OF_PRODUCT)

    def get_features_of_product(self):
        return self._get_elements(locator.FEATURES_OF_PRODUCT)

    def get_image_of_product(self):
        return self._get_element(locator.IMG_PRODUCT)

    def get_price_of_product(self):
        return self._get_element(locator.PRICE)

    def get_currency(self):
        return self._get_element(locator.CURRENCY)