from selenium.webdriver import ActionChains

from pageObject.MenAccessoriesOb import TestMenAccessoriesOb
from utilities.BaseClass import BaseClass


class TestMenAccessories(BaseClass):

    def test_MenAccer(self):
        log = self.getLogger()

        menAcc = TestMenAccessoriesOb(self.driver)

        log.info("'Moving to options to get MEN option")
        menAcc.qstartOption()

        self.hover(menAcc.qhaverOn())
        log.info("Hover on option Men option")


        menAcc.qcatogory()
        text = menAcc.getText()

        log.info(text + " is selected")
        menAcc.qselectItm()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in menAcc.productNameVerify())
        log.info(menAcc.productNameVerify() + " is displaying in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")

