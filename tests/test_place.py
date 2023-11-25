import time

from pageObject.PlaceOrder import test_order
from utilities.BaseClass import BaseClass


class TestPlace(BaseClass):

    def test_place(self):
        log = self.getLogger()
        Ord = test_order(self.driver)
        Ord.test_bar()
        log.info("for entering the data in search bar")

        Ord.test_click()
        log.info("for search bar")
        Ord.test_bottle()
        log.info("clicks on bottle")

        self.childBrowser()
        log.info("handles tab")

        Ord.test_addtocart()
        log.info("add to cart ")
        Ord.test_place()
        log.info("place the order")
        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
