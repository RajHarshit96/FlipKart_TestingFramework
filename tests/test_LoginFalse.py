import pytest
from selenium.webdriver import ActionChains

from TestData.LoginFalseDATA import LoginFalseData
from pageObject.LoginFalse import TestLoginFal
from utilities.BaseClass import BaseClass


class TestLoginFalse(BaseClass):

    def test_NewAddress(self, getData):
        log = self.getLogger()
        LogFail = TestLoginFal(self.driver)

        self.hover(LogFail.qhover())
        log.info("Child window switched")

        LogFail.qlogout()
        log.info("Logged out successfully")

        LogFail.quserName().send_keys(getData["username"])
        log.info("username Entered")
        LogFail.qPassword().send_keys(getData["FalsePassword"])
        log.info("Password Entered")

        LogFail.qsubmit()
        log.info("Submitted")

        assert ("incorrect" in LogFail.qpromt())
        log.info(LogFail.qpromt()+" shown Successfully")

    @pytest.fixture(params=LoginFalseData.test_FalseLog_data)
    def getData(self, request):
        return request.param