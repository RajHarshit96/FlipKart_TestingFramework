import time

from selenium.webdriver import ActionChains

from pageObject.Router import test_Router
from utilities.BaseClass import BaseClass


class TestRouter(BaseClass):

    def test_rou(self):
        log = self.getLogger()
        ec = test_Router(self.driver)
        ec.test_items()
        log.info("clicks electronics")

        a = ActionChains(self.driver)
        a.move_to_element(ec.test_hover()).perform()
        log.info("mouse hover in electronics")
        time.sleep(3)

        a.move_to_element(ec.test_rout()).click().perform()
        log.info("click on router")
        time.sleep(5)

        ec.test_product()
        log.info("click on product")

        self.childBrowser()
        log.info("tab handle")

        ec.test_buy()
        log.info("buy now")
        time.sleep(2)
        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
