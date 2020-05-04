from locators.goodnotes_help_center_locators import Locators as gn_hc
from locators.goodnotes_help_center_results_page_locators import Locators as gn_hcp
from selenium.webdriver.common.keys import Keys


class GoodNotesHelpCenterPage:

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.maximize_window()
        self.browser.get('https://support.goodnotes.com/hc/en-us')

    def validate(self):
        assert self.browser.find_element(*gn_hc.search_box).is_displayed()

    def search(self, word):
        search_box = self.browser.find_element(*gn_hc.search_box)
        search_box.send_keys(word + Keys.ENTER)
        assert self.browser.find_element(*gn_hcp.results).is_displayed()
        assert len(self.browser.find_elements(*gn_hcp.results)) > 0
