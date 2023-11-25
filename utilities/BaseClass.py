import pytest
import inspect
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

# Method to Log comments in log file
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C:\\Users\\HARSHRAJ\\PycharmProjects\\Sprint_2_Flipkart\\reports\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def childBrowser(self):

        ChildWindow = self.driver.window_handles[1]
        self.driver.switch_to.window(ChildWindow)

    def hover(self,m):
        a = ActionChains(self.driver)
        a.move_to_element(m).perform()
