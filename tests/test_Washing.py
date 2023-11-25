import time

from selenium.webdriver import ActionChains

from pageObject.WashingMachine import TestWashingMachine
from utilities.BaseClass import BaseClass


class TestFullyAutomaticWashing(BaseClass):

    def test_AutomaticMachine(self):
        log = self.getLogger()

        autoWash =TestWashingMachine(self.driver)
        time.sleep(5)

        log.info("'Moving to option to get TVs & Appliances option")
        autoWash.initialfirstOption()

        self.hover(autoWash.catlogSelect())
        log.info("Hover on option TVs & Appliances")


        time.sleep(4)
        autoWash.IteamCatagorySelection()
        text = autoWash.getText()

        log.info(text + " is selected")
        autoWash.click_iteam()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in autoWash.productNameVerify())
        log.info(autoWash.productNameVerify() + " is displayed in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")

