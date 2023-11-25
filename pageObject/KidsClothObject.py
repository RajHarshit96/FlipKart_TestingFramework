from selenium.webdriver.common.by import By


class TestKids:
    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    startOption = (By.XPATH, "//div[.='Mobiles']")
    kidsCatlog = (By.XPATH, "//span[.='Baby & Kids']")
    selectIteamCatagoty = (By.XPATH, "//a[.='Dresses & Skirts']")
    selectIteam = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/div/a[1]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]")

    # Function to be called in testCases
    def qstartOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestKids.startOption).click()

    def qkidsCatlog(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestKids.kidsCatlog)

    def qselectIteamCatagoty(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestKids.selectIteamCatagoty).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        text = self.driver.find_element(*TestKids.selectIteam).text
        return text

    def qselectIteam(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestKids.selectIteam).click()

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestKids.productVerifyMsg).text
        return msg







