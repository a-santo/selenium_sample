import pytest

from selenium.webdriver import Chrome
from pages import goodnotes_help_center_page


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_search(browser):
    search_page = goodnotes_help_center_page.GoodNotesHelpCenterPage(browser)
    search_page.load()
    search_page.search('how to search')
