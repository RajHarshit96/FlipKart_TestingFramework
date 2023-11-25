import time

from pageObject.Order_Product import TestOrder_Product
from utilities.BaseClass import BaseClass


class TestPrdk(BaseClass):

    def test_OrderProduct(self):
        log = self.getLogger()

        orderPt = TestOrder_Product(self.driver)
        time.sleep(5)
        log.info("Searching iphone 13 pro max in search bar")
        orderPt.searchIteam()
        orderPt.clickToSearch()


        orderPt.lookForProduct()
        log.info("Iphone is selected")

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        orderPt.clickBuynow()
        log.info("Click On Buy now")

        orderPt.selectAddress()
        log.info("Continue for Address")
        orderPt.goToPayment()
        log.info("Procced to payment")
        #orderPt.acceptCondition()
        log.info("Now Product can be ordered successfully")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")



