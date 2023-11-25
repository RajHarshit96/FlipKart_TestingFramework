import time

from selenium.webdriver import ActionChains

from pageObject.SkinCareOb import TestSkinCareOb

from utilities.BaseClass import BaseClass


class TestSkinCare(BaseClass):

    def test_skinCare(self):
        log = self.getLogger()
        hSkinC = TestSkinCareOb(self.driver)
        time.sleep(5)
        log.info("Women options is Invoked for Skin Care")
        hSkinC.initialfirstOption()

        self.hover(hSkinC.qhover())
        log.info("Hover on option Women")


        time.sleep(4)
        hSkinC.IteamCatagorySelection()
        text = hSkinC.getText()

        log.info(text + " is selected")
        hSkinC.click_iteam()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in hSkinC.productNameVerify())
        log.info(hSkinC.productNameVerify() + " is displayed in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")