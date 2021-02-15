from pages.AdminPage import AdminPage
from pages.BasePage import BasePage
from pages.locators import LoginPageLocators as locator


class LoginPage(BasePage):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        super(LoginPage, self).__init__(self.driver,
                                        self.url)

    def get_form_header(self):
        return self._get_element(locator.HEADER)

    def get_input_username(self):
        return self._get_element(locator.FIELD_USERNAME)

    def get_input_password(self):
        return self._get_element(locator.FIELD_PASSWORD)

    def get_button_login(self):

        return self._get_element(locator.BUTTON_LOGIN)

    def get_forgotten_password_link(self):
        return self._get_element(locator.LINK_FORGOTTEN_PASSWORD)

    def login(self, username, password):
        self.get_input_username().send_keys(username)
        self.get_input_password().send_keys(password)
        self.get_button_login().click()
        return AdminPage(driver=self.driver, base_url=None, prev_page=self)

    def get_notification(self):
        return self._get_element(locator.NOTIFICATION)