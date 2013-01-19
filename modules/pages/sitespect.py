"""
=============
SiteSpectPage
=============
"""
from tailored.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

import time


class SiteSpectPage(Page):
    """
    PO for the SiteSpect page
    """
    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def open_default_url(self):
        self.driver.get("https://sitespect.walmart.com")
        time.sleep(6)
