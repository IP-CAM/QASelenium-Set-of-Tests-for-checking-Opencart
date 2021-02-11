from pages.components.Component import Component


class Search(Component):
    SEARCH_INPUT = {'css': '#search > input'}
    SEARCH_BUTTON = {'css': '#search > span > button'}

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
