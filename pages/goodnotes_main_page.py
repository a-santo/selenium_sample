from locators.goodnotes_main_page_locators import Locators as gn_main
from locators.itunes_goodnotes_locators import Locators as itunes_loc


class GoodNotesMainPage:

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.maximize_window()
    self.browser.get('https://www.goodnotes.com/')

  def fetch_copyright_notice(self):
    return self.browser.find_element(*gn_main.copyright_notice)

  def validate(self):
    assert self.browser.find_element(*gn_main.copyright_notice).is_displayed()

  def click_features(self):
    self.browser.find_element(*gn_main.features_nav_link).click()

  def click_help_center(self):
    self.browser.find_element(*gn_main.help_center_nav_link).click()

  def click_blog(self):
    self.browser.find_element(*gn_main.blog_nav_link).click()

  def click_get_app(self):
    self.browser.find_element(*gn_main.get_app_nav_link).click()
    assert self.browser.find_element(*itunes_loc.icon).is_displayed()

#def abrir_menu_principal(self):
  #  menu = self.browser.find_element(*rpp_loc.menu_principal)
  #  menu.click()

  #def pesquisar(self, palavra):
  #  caixa = self.browser.find_element(*rpp_loc.cx_pesquisa)
  #  caixa.send_keys(palavra + Keys.ENTER)
  #  assert self.browser.find_element(*rpp_loc.div_class_centro).is_displayed()
