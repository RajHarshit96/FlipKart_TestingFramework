import time

from selenium.webdriver import ActionChains

from pageObject.television import TestTelevision
from utilities.BaseClass import BaseClass


class TestTV(BaseClass):

    def test_Tv(self):
        log = self.getLogger()
        prdTV = TestTelevision(self.driver)

        time.sleep(5)

        log.info("'Moving to option to get TVs & Appliances option")
        prdTV.optionOne()

        self.hover(prdTV.hover())
        log.info("Hover on option TVs & Appliances")


        prdTV.click_tv().click()
        text = prdTV.getText()

        log.info(text + " is selected")
        prdTV.selectPRODUCT()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in prdTV.productNameVerify())
        log.info(prdTV.productNameVerify() + " is displayed in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")


