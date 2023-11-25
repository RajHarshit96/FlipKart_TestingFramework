import time

from selenium.webdriver import ActionChains


from pageObject.WomenHandBagOb import TestWomenHandBagOb

from utilities.BaseClass import BaseClass


class TestWomenHandBag(BaseClass):

    def test_womenBag(self):
        log = self.getLogger()

        bag = TestWomenHandBagOb(self.driver)
        time.sleep(5)
        log.info("Women options is Invoked for Handbag")
        bag.initialfirstOption()

        self.hover(bag.qhover())
        log.info("Hover on option Women")


        time.sleep(4)
        bag.IteamCatagorySelection()
        text = bag.getText()

        log.info(text + " is selected")
        bag.click_iteam()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in bag.productNameVerify())
        log.info(bag.productNameVerify() + " is displayed in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")