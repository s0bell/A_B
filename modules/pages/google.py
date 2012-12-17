"""
==========
GooglePage
==========
"""
from tailored.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'search box': 'name=q',
    'search btn': 'name=btnK'
}


class GooglePage(Page):
    """
    PO for the Google page
    """
    def __init__(self, driver):
        self.locators = locators
        self.driver = driver
        self.config = cfg_wrapper().config

    def open_default_url(self):
        self.driver.get("http://www.google.com")

    def search_for(self, query):
        self.driver.find_element_by_locator(
            locators['search box']).send_keys(query)

    def click_result_title(self, title):
        self.driver.find_element_by_locator('link=%s' % title).click()
