import time

from pageObject.RoundTrip import test_Round
from utilities.BaseClass import BaseClass


class TestFlight(BaseClass):

    def test_search(self):
        log = self.getLogger()
        Round = test_Round(self.driver)

        Round.test_travel()
        log.info("click on travel")
        time.sleep(5)

        Round.test_full()
        log.info("for round trip button")
        time.sleep(5)

        Round.test_search()
        log.info("clicks on search")
        time.sleep(10)

        Round.test_change()
        log.info("changes the flight")
        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
