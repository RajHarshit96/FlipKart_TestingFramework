import time

from selenium.webdriver import ActionChains

from pageObject.HomeFurnitureObject import TestHomef
from utilities.BaseClass import BaseClass
class TestHomeFurniture(BaseClass):

    def test_homeFurniture(self):
        log = self.getLogger()

        homeFur = TestHomef(self.driver)
        time.sleep(5)

        log.info("'Home & Furniture options is Invoked for Bean Bag")
        homeFur.initialfirstOption()

        self.hover(homeFur.qhover())
        log.info("Hover on option Home & Furniture")


        time.sleep(4)
        homeFur.IteamCatagorySelection()
        text = homeFur.getText()

        log.info(text + " is selected")
        homeFur.click_iteam()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")


        assert (text in homeFur.productNameVerify())
        log.info(homeFur.productNameVerify() + " is displayed in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")



