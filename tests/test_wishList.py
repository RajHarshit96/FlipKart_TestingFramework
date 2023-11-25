import time

from pageObject.WishList import test_wish
from utilities.BaseClass import BaseClass


class TestBar(BaseClass):

    def test_bar(self):
        log = self.getLogger()
        w = test_wish(self.driver)

        w.test_sb()

        w.test_click()
        log.info("click")
        w.test_x()

        self.childBrowser()
        log.info("handles tab")

        w.test_ish()
        log.info("add wish list")
        time.sleep(5)
        w.test_eh()
        log.info("add remove wish list")
        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
