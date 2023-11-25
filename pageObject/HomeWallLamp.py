from selenium.webdriver.common.by import By


class TestHomeWallLampOb:
    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    startOption = (By.XPATH, "//div[.='Mobiles']")
    kidsCatlog = (By.XPATH, "//span[.='Home & Furniture']")
    selectIteamCatagoty = (By.XPATH, "//a[.='Wall Lamp']")
    selectIteam = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")

    # Function to be called in testCases
    def initialfirstOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestHomeWallLampOb.startOption).click()

    def qhover(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestHomeWallLampOb.kidsCatlog)

    def IteamCatagorySelection(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestHomeWallLampOb.selectIteamCatagoty).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        text = self.driver.find_element(*TestHomeWallLampOb.selectIteam).text
        return text

    def click_iteam(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestHomeWallLampOb.selectIteam).click()

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestHomeWallLampOb.productVerifyMsg).text
        return msg
