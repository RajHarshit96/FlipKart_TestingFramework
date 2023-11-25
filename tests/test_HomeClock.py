import time

from selenium.webdriver import ActionChains

from pageObject.HomeFurClockObject import TestHomeClock
from utilities.BaseClass import BaseClass


class TestHomeClockkk(BaseClass):

    def test_homeClock(self):
        log = self.getLogger()
        homeClk = TestHomeClock(self.driver)
        time.sleep(5)
        log.info("'Home & Furniture options is Invoked for clock")
        homeClk.initialfirstOption()

        self.hover(homeClk.qhover())
        log.info("Hover on option Home & Furniture")


        time.sleep(4)
        homeClk.IteamCatagorySelection()
        text = homeClk.getText()

        log.info(text + " is selected")
        homeClk.click_iteam()


        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in homeClk.productNameVerify())
        log.info(homeClk.productNameVerify() + " is displaying in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")