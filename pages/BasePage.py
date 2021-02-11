from pages import Component


class BasePage(Component):
    def __init__(self, driver, url):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
