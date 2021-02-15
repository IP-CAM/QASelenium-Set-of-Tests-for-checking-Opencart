from pages.components.Component import Component


class Footer(Component):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
