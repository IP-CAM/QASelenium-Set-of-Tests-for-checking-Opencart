from pages.components.Component import Component


class CartPage(Component):
    SEARCH_BUTTON = {'css': '#cart > button'}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
