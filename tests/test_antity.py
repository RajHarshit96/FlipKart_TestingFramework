import time

from pageObject.Quantity import test_quant
from utilities.BaseClass import BaseClass


class TestQuantity(BaseClass):

    def test_quantity(self):
        log = self.getLogger()
        t = test_quant(self.driver)
        t.test_bar()
        log.info("for entering the data in search bar")

        t.test_click()
        log.info("for search bar")
        t.test_aero()
        log.info("takes aeroplane as input")

        self.childBrowser()
        log.info("Window Switched")

        t.test_cart()
        log.info("add to cart")       #getting error in cmd  resolved fail
        time.sleep(5)

        t.scroll()

        time.sleep(4)
        t.test_clear()
        log.info("increases quantity")
        time.sleep(5)                                       # fail
        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
