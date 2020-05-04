import pytest
import datetime

from selenium.webdriver import Chrome
from pages import goodnotes_main_page, goodnotes_features_page, goodnotes_help_center_page, goodnotes_blog_page


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_copyright_message(browser):
    main_page = goodnotes_main_page.GoodNotesMainPage(browser)
    main_page.load()
    msg = main_page.fetch_copyright_notice()
    assert msg.is_displayed()
    # assert '2018' in msg.text
    assert str(datetime.datetime.now().year) in msg.text


def test_nav_menu(browser):
    main_page = goodnotes_main_page.GoodNotesMainPage(browser)
    main_page.load()
    main_page.validate()
    features_page = goodnotes_features_page.GoodNotesHelpCenterPage(browser)
    main_page.click_features()
    features_page.validate()
    browser.back()
    main_page.validate()
    hc_page = goodnotes_help_center_page.GoodNotesHelpCenterPage(browser)
    main_page.click_help_center()
    hc_page.validate()
    browser.back()
    main_page.validate()
    main_page.click_blog()
    blog_page = goodnotes_blog_page.GoodNotesMainPage(browser)
    # store the current and new tab/window
    original_tab = browser.window_handles[0]
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    blog_page.validate()
    browser.close()
    # go back to the original tab
    browser.switch_to.window(original_tab)
    main_page.validate()
    main_page.click_get_app()
