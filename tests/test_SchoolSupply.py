import time

from selenium.webdriver import ActionChains

from pageObject.SchoolSupplies import TestSchoolSuppliesOb
from utilities.BaseClass import BaseClass


class TestSchoolSupply(BaseClass):

    def test_schoolsply(self):
        log = self.getLogger()

        schlSup = TestSchoolSuppliesOb(self.driver)

        log.info("'Moving to options to get Baby & Kids option")
        schlSup.qstartOption()

        self.hover(schlSup.qkidsCatlog())
        log.info("Hover on option Baby & Kids option")

        schlSup.qselCatagory()
        time.sleep(4)

        test = schlSup.getText()
        log.info(test + " is selected")

        schlSup.qselectItm()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (test in schlSup.productNameVerify())
        log.info(schlSup.productNameVerify() + " is displaying in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")
