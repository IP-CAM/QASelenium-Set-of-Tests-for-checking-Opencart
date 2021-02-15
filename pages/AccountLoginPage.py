from pages.BasePage import BasePage
from pages.locators.AccountLoginPageLocators import AccountLoginPageLocators as locator


class AccountLoginPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        super(AccountLoginPage, self).__init__(self.driver,
                                               self.url)

    def get_button_continue(self):
        return self._get_element(locator.BUTTON_NEW_CUSTOMER_CONTINUE)

    def get_field_username_of_returned_customer(self):
        return self._get_element(locator.INPUT_EMAIL)

    def get_field_password_of_returned_customer(self):
        return self._get_element(locator.INPUT_PASSWORD)

    def get_button_login_of_returned_customer(self):
        return self._get_element(locator.BUTTON_LOGIN)

    def get_text_header_of_block_new_customer(self):
        return self._get_element_text(locator.HEADER_NEW_CUSTOMER)

    def get_text_header_of_block_returned_customer(self):
        return self._get_element_text(locator.HEADER_RETURNING_CUSTOMER)

    def login_returned_customer(self, name, password):
        self.get_field_username_of_returned_customer().send_keys(name)
        self.get_field_password_of_returned_customer().send_keys(password)
        self.get_button_login_of_returned_customer().click()
