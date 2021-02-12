from pages.BasePage import BasePage


class AdminPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url  # TODO поправить на корректный url
        super(AdminPage, self).__init__(self.driver,
                                        self.url)
