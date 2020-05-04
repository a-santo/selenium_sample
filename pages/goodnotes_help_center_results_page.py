from locators.goodnotes_help_center_results_page_locators import Locators as gn_hcr


class GoodNotesHelpCenterResultsPage:

    def __init__(self, browser):
        self.browser = browser

    def is_valid(self):
        assert self.browser.find_element(*gn_hcr.results).is_displayed()
