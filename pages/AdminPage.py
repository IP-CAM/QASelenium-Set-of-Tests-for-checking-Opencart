from pages.BasePage import BasePage
from pages.locators.AdminPageLocators import AdminPageLocators as locator


class AdminPage(BasePage):
    def __init__(self, driver, base_url=None, prev_page=None):
        self.driver = driver
        self.url = base_url
        self.prev_page = prev_page
        super(AdminPage, self).__init__(self.driver,
                                        self.url)

    def get_logout_link(self):
        return self._wait_for_visible(locator.LOGOUT, wait=10)

    def logout(self):
        self.get_logout_link().click()
        return self.prev_page

    def get_profile(self):
        return self._get_element(locator.PROFILE)

    def get_left_menu_top_items(self):
        return self._get_elements(locator.MENU_TOP_ITEMS)

    def get_top_item_in_left_menu_by_name(self, path_menu: str):
        raw_items = path_menu.split('>')
        for item in list(map(str.strip, raw_items)):
            xpath = f'//*[@id="menu"]//a[contains(text(), "{item}")]'
            find = {'xpath': xpath}
            el = self._wait_for_visible(find)
            el.click()

    def get_product_table(self):
        return self._get_element(locator.PRODUCT_TABLE)

    def get_product_table_headers(self):
        return self._get_elements(locator.COLUMNS_OF_HEAD_TABLE)