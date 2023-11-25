import time

from pageObject.Mobile import test_Mobile
from utilities.BaseClass import BaseClass


class TestMob(BaseClass):

    def test_mobile(self):
        log = self.getLogger()
        m = test_Mobile(self.driver)
        m.test_mobiles()
        log.info("click on mobiles")

        m.test_play()
        log.info("click on Infinix hot 12 play")

        m.test_gb()
        log.info("click on Infinix hot 12 play 64gb")

        self.childBrowser()
        log.info("Handles tab")

        m.test_crt()
        log.info("add to cart")
        time.sleep(5)
        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
