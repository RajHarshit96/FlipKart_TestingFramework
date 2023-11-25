import time

from selenium.webdriver import ActionChains

from pageObject.KidsClothObject import TestKids
from utilities.BaseClass import BaseClass


class TestKidsMain(BaseClass):

    def test_kidsCloth(self):
        log = self.getLogger()

        kidsTKC = TestKids(self.driver)

        log.info("'Kids options is Invoked for Kids Cloth")
        kidsTKC.qstartOption()

        self.hover(kidsTKC.qkidsCatlog())
        log.info("Hover on option Baby & Kids")


        kidsTKC.qselectIteamCatagoty()
        text = kidsTKC.getText()

        log.info(text + " is selected")
        kidsTKC.qselectIteam()

        self.childBrowser()
        log.info("Successfully switched to the child-tab")

        assert (text in kidsTKC.productNameVerify())
        log.info(kidsTKC.productNameVerify() + " is displaying in detail and verified")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")




