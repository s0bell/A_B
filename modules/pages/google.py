"""
==========
GooglePage
==========
"""
from tailored.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'search box': 'name=q',
    'search btn': 'name=btnK',
    'result set': 'css=#rso li.g:nth-child(N) a.l'
}


class GooglePage(Page):
    """
    PO for the Google page
    """
    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def open_default_url(self):
        self.driver.get("http://www.google.com")

    def search_for(self, query):
        self.driver.find_element_by_locator(
            locators['search box']).send_keys(query)

    def click_result(self, index):
        self.driver.find_element_by_locator(
            locators['result set'].replace('N', str(index))).click()
        #self.wait_for_jquery_active()

    def redirect(self, url):
        u = "http://www.google.com/url?rct=j&q=this&url={0}".format(url)
        self.driver.get(u)
        self.driver.find_element_by_link_text(url).click()
