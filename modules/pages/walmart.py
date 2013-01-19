"""
===========
WalmartPage
===========
"""
from urlparse import urlparse
from tailored.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

import collections
import cgi

locators = {
    "control recs": "css=#rr_placement_0 a.BodyM",
    "variant recs": "css=a.BodyMBold"
}


class WalmartPage(Page):
    """
    PO for the Walmart page
    """
    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def open_default_url(self):
        self.driver.get("http://www.walmart.com")

    def open_variant_preview_url(self):
        self.driver.get("http://www.walmart.com/?SS_PREVIEW_EXP=2013_FEB_13_1700PST&ChEDr_oTrAFfrhCPGXeArAdyCArPsXrvs78MrD8PpAS0G7KvGhULGOr=CPrgG73PsA3gBTs6EXecOSdHCfp_rnB6rno6NM0tKDHQKiHBo7v=sArgsyp_oQHsNMo6pDTTp8H1khUgChCuC78uChSYC78JC7UJCAKDeXePE8sFNnaF9_E1nvT8khrPsypXE_=2StBTEDTTEPv=BTaypnp6pnEdNZaeKisTEto6NDKHCypBpM0qKDeh9noTeDiy9_iv9_H1KPvgBVTRNDHypSF6pMFTKTsTKes6EXe_rnB6rno6NM0Pkh3DO_E1NZBTSne6rMu79Xi1pMePkh3DSDeDpnBTKAvDensTStBTEDTTEviPKMTPEXi1E7vgBTaypnp6pnEibXs2E_oTSTa_nvT8kh3")

    def open_control_preview_url(self):
        self.driver.get("http://www.walmart.com/?SS_PREVIEW_EXP=2013_JAN_11_2300GMT&p7iVCAULrPFAsMiFs_UZG73MrMrPphiTr_8LpAEfp7rvC_oTrMeTpfr=CPSZGhdQCA3gBTs6EXecOSdHCfp_rnB6rno6NM0tKDHQKiHBo7v=sArgsfp_oQHsNMo6pDTTp8H1khUgChUuChUuCh3YCAUJCACJs7rDeXePE8sFNnaF9_E1nvT8khrPsypXE_=2StBTEDTTEPv=BTaypnp6pnEdNZaeKisTEto6NDKHCypBpM0qKDeh9noTeDiy9_iv9_H1KPvgBVTRNDHypSF6pMFTKTsTKes6EXe_rnB6rno6NM0Pkh3DO_E1NZBTSne6rMu79Xi1pMePkh3DSDeDpnBTKAvDensTStBTEDTTEviPKMTPEXi1E7vgBTaypnp6pnEibX\s2E_oTSTa_nvT8kh3")

    def set_control_cookie(self):
        cookie = {
            "name": "SSSC",
            "value": "2.G5821861928406243841.1|637.16606",
            "domain": ".walmart.com",
            "path": "/"
        }
        self.driver.delete_all_cookies()
        self.driver.add_cookie(cookie)

    def set_variant_cookie(self):
        cookie = {
            "name": "SSSC",
            "value": "2.G5821861928406243841.1|637.16607",
            "domain": ".walmart.com",
            "path": "/"
        }
        self.driver.delete_all_cookies()
        self.driver.add_cookie(cookie)
        #all_cookies = self.driver.get_cookies()
        #for cookie_name in all_cookies:
        #    print cookie_name
        #import sys
        #sys.exit()

    def get_control_recommendations(self):
        results = []
        recs = self.driver.find_elements_by_locator(locators['control recs'])
        rank = 1
        for r in recs:
            href = r.get_attribute('href')
            hr = dict(cgi.parse_qsl(href))
            d = collections.OrderedDict()
            d['rank'] = rank
            d['product_id'] = hr['p']
            d['title'] = r.text
            d['id'] = urlparse(href).netloc
            results.append(d)
            rank += 1
        return results

    def get_variant_recommendations(self):
        results = []
        recs = self.driver.find_elements_by_locator(locators['variant recs'])
        rank = 1
        for r in recs:
            aid = r.get_attribute('id')
            x = aid.split('_')[:-1]
            uid = '_'.join(x)
            d = collections.OrderedDict()
            d['rank'] = rank
            d['product_id'] = aid.split('_')[-1]
            d['title'] = r.text
            d['id'] = uid
            results.append(d)
            rank += 1
        return results

    def accept_alert(self):
        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
        except:
            pass

    def save_screenshot(self, name):
        self.driver.get_screenshot_as_file('{0}_screenshot.png'.format(name))
