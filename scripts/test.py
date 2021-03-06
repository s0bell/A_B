from saunter.testcase.webdriver import SaunterTestCase

from pages.sitespect import SiteSpectPage
from pages.google import GooglePage
from pages.control import ControlPage
from pages.variant import VariantPage

import pytest


class TestMain(SaunterTestCase):
    @pytest.marks('deep')
    def test_control(self):
        # Load the control page
        c = ControlPage(self.driver)
        c.open_default_url()

        # Execute the google search and click our result
        g = GooglePage(self.driver)
        g.open_default_url()
        g.search_for('canon t2i walmart')
        g.click_result_title(
            'Canon DSLR Camera, EOS Rebel T2i, 18-55mm Lens - Walmart.com')

        # Save screenshot to disk
        #c.save_screenshot()

    @pytest.marks('shallow')
    def test_variant1(self):
        # Make connection with SiteSpect
        #s = SiteSpectPage(self.driver)
        #s.open_default_url()
        
        v = VariantPage(self.driver)
        # Load the variant preview
        #v.open_preview_url()
        #v.accept_alert()

        # Set the variant cookie
        v.open_default_url()
        v.set_cookie()
        import sys, time

        referer = {"referer": "http://www.google.com?q=anything"}
        self.client.headers(referer)
        
        self.driver.get("http://www.walmart.com/ip/20604608")
        time.sleep(60)
        sys.exit()

        # Execute the google search and click our result
        self.client.new_har("google")
        g = GooglePage(self.driver)
        g.open_default_url()
        g.search_for('canon t2i walmart')
        g.click_result_title(
            'Canon DSLR Camera, EOS Rebel T2i, 18-55mm Lens - Walmart.com')

        #v.accept_alert()
        #v.accept_alert()
        #v.accept_alert()
        h = self.client.har()
        #import json
        #print json.dumps(h)
        

        proxy.close()
        driver.quit()
        import sys
        sys.exit()
        # Save screenshot to disk
        #v.save_screenshot()
