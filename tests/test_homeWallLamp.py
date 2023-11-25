import time

from selenium.webdriver import ActionChains

from pageObject.HomeWallLamp import TestHomeWallLampOb
from utilities.BaseClass import BaseClass


class TestHomeWallLamp(BaseClass):

    def test_homeWallLamppp(self):
        log = self.getLogger()


        homeFur = TestHomeWallLampOb(self.driver)
        time.sleep(5)
        log.info("'Home & Furniture options is Invoked for Wall Lamp")
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