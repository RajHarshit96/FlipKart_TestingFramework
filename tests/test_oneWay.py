import time

from pageObject.OneWay import test_OneWay
from utilities.BaseClass import BaseClass


class TestBombay(BaseClass):

    def test_way(self):
        log = self.getLogger()
        plane = test_OneWay(self.driver)
        plane.test_travel()
        log.info("click on travel")
        time.sleep(5)

        plane.test_way()
        log.info("select one way")
        time.sleep(5)

        plane.test_search()
        log.info("clicks on search")

        plane.test_details()
        log.info("click on details")
        time.sleep(5)

        plane.test_book()
        log.info("clicks on book")

        plane.test_continue()
        log.info("clicks on continue")


        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
