from locators.goodnotes_blog_locators import Locators as blog_loc

class GoodNotesMainPage:

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.maximize_window()
        self.browser.get('https://medium.goodnotes.com/')

    def validate(self):
        assert self.browser.find_element(*blog_loc.main_header_link).is_displayed()