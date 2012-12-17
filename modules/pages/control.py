"""
===========
ControlPage
===========
"""
from tailored.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper


class ControlPage(Page):
    """
    PO for the Control page
    """
    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def open_preview_url(self):
        self.driver.get("http://www.walmart.com/?SS_PREVIEW_EXP=2013_JAN_11_2300GMT&p7iVCAULrPFAsMiFs_UZG73MrMrPphiTr_8LpAEfp7rvC_oTrMeTpfr=CPSZGhdQCA3gBTs6EXecOSdHCfp_rnB6rno6NM0tKDHQKiHBo7v=sArgsfp_oQHsNMo6pDTTp8H1khUgChUuChUuCh3YCAUJCACJs7rDeXePE8sFNnaF9_E1nvT8khrPsypXE_=2StBTEDTTEPv=BTaypnp6pnEdNZaeKisTEto6NDKHCypBpM0qKDeh9noTeDiy9_iv9_H1KPvgBVTRNDHypSF6pMFTKTsTKes6EXe_rnB6rno6NM0Pkh3DO_E1NZBTSne6rMu79Xi1pMePkh3DSDeDpnBTKAvDensTStBTEDTTEviPKMTPEXi1E7vgBTaypnp6pnEibX\s2E_oTSTa_nvT8kh3")

    def open_default_url(self):
        self.driver.get("http://www.walmart.com")

    def set_cookie(self):
        cookie = {
            "name": "SSSC",
            "value": "2.G5821861928406243841.1|637.16606",
            "domain": ".walmart.com",
            "path": "/"
        }
        self.driver.add_cookie(cookie)

    def save_screenshot(self):
        self.driver.get_screenshot_as_file('control_screenshot.png')
