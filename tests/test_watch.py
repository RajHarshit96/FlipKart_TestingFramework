import time

from selenium.webdriver import ActionChains

from pageObject.SmartWatch import test_HomePage
from utilities.BaseClass import BaseClass


class TestEce(BaseClass):

    def test_you(self):
        log = self.getLogger()
        homePage = test_HomePage(self.driver)
        homePage.test_shopItems()
        log.info("click on electronics icon")

        a = ActionChains(self.driver)
        time.sleep(5)
        a.move_to_element(homePage.test_hover()).perform()
        log.info("mouse hover in electronics")

        a.move_to_element(homePage.test_watch()).click().perform()
        log.info("clicks on smart watch")
        time.sleep(5)

        homePage.test_apple()
        log.info("clicks on apple watch")

        self.childBrowser()
        log.info("handles tab")

        homePage.test_buyNow()
        log.info("click on buy now")
        time.sleep(3)
        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
