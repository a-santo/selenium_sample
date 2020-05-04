from selenium.webdriver.common.by import By


class Locators:
    copyright_notice = (By.CSS_SELECTOR, '.col-sm-4.pull-left')
    features_nav_link = (By.CSS_SELECTOR, 'div#navbar > ul > li:nth-of-type(1) > a')
    help_center_nav_link = (By.CSS_SELECTOR, 'div#navbar > ul > li:nth-of-type(2) > a')
    blog_nav_link = (By.CSS_SELECTOR, "div#navbar a[target='_blank']")
    get_app_nav_link = (By.CSS_SELECTOR, '.callout > a')
