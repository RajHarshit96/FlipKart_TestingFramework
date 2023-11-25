import time

from selenium.webdriver import ActionChains

from pageObject.KidsToyObject import TestToys
from utilities.BaseClass import BaseClass


class TestKidsToysMain(BaseClass):

    def test_kidToy(self):
        log = self.getLogger()

        log.info("'Kids options is Invoked for Kids Toys")
        toys = TestToys(self.driver)

        toys.qstartOption()

        self.hover(toys.qkidsCatlog())
        log.info("Hover on option Baby & Kids")

        toys.qselCatagory()

        text = toys.getText()
        log.info(text + " is selected")
        toys.qselectItm()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in toys.productNameVerify())
        log.info(toys.productNameVerify() + " is displaying in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")