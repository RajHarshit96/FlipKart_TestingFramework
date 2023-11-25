import time

from pageObject.Remove import test_removes
from utilities.BaseClass import BaseClass


class TestRemove(BaseClass):

    def test_remove(self):
        log = self.getLogger()
        a = test_removes(self.driver)

        a.test_cart()
        log.info("click on cart")
        time.sleep(5)

        a.test_remove()
        log.info("clicks on remove")
        time.sleep(5)

        a.test_item()
        log.info("removes item from cart")
        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
