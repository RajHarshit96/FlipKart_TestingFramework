import time

from selenium.webdriver import ActionChains


from pageObject.WomewntopWearOb import TestWomenTopOb

from utilities.BaseClass import BaseClass


class TestWomenTopW(BaseClass):

    def test_topWear(self):
        log = self.getLogger()

        wear = TestWomenTopOb(self.driver)
        time.sleep(5)
        log.info("Women options is Invoked for Topwear")
        wear.initialfirstOption()

        self.hover(wear.qhover())
        log.info("Hover on option Women")

        time.sleep(4)
        wear.IteamCatagorySelection()
        text = wear.getText()

        log.info(text + " is selected")
        wear.click_iteam()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in wear.productNameVerify())
        log.info(wear.productNameVerify() + " is displayed in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")