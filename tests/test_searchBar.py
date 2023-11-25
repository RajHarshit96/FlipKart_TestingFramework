import time

from pageObject.Searchbar import test_search
from utilities.BaseClass import BaseClass


class TestBar(BaseClass):

    def test_bar(self):
        log = self.getLogger()
        search = test_search(self.driver)
        search.test_sbar()
        log.info("for entering the data in search bar")

        search.test_click()
        log.info("for search bar")
        search.test_jeans()                                         # sold out
        log.info("takes jeans as input")

        text = search.getText()

        self.childBrowser()
        log.info("handles tab")



        assert (text in search.productNameVerify())

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
