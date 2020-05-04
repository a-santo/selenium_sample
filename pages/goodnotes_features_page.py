from locators.goodnotes_features_locators import Locators as features_loc


class GoodNotesHelpCenterPage:

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.maximize_window()
        self.browser.get('https://www.goodnotes.com/features/')

    def validate(self):
        assert self.browser.find_element(*features_loc.main_image).is_displayed()