from selenium.webdriver import ActionChains

from pageObject.MenGroomObject import TestMenGrm
from utilities.BaseClass import BaseClass


class TestMenGrooming(BaseClass):

    def test_TestMenGrming(self):
        log = self.getLogger()

        menGrm = TestMenGrm(self.driver)

        log.info("'Moving to options to get MEN option")
        menGrm.qstartOption()

        self.hover(menGrm.qhaverOn())
        log.info("Hover on option Men option")


        menGrm.qcatogory()
        text = menGrm.getText()

        log.info(text + " is selected")
        menGrm.qselectItm()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in menGrm.productNameVerify())
        log.info(menGrm.productNameVerify() + " is displaying in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")