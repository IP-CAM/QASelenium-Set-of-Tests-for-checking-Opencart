from pages import Component


class BasePage(Component):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        super(BasePage, self).__init__(driver)

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
