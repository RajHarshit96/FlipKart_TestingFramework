import time

from selenium.webdriver import ActionChains

from pageObject.MenFootwareObject import TestMenFootOb
from utilities.BaseClass import BaseClass
import warnings



class TestMenFootware(BaseClass):

    def test_MenFootware(self):
        log = self.getLogger()

        kidsFoot = TestMenFootOb(self.driver)
        time.sleep(5)

        log.info("'Moving to options to get MEN option")
        kidsFoot.qstartOption()

        self.hover(kidsFoot.qkidsCatlog())
        log.info("Hover on option Men option")


        kidsFoot.qqIteamCatagory()

        Ttext = kidsFoot.getText()

        log.info(Ttext + " is selected")
        kidsFoot.qqseletIteam()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")


        assert (Ttext in kidsFoot.productNameVerify())
        log.info(kidsFoot.productNameVerify() + " is displaying in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")