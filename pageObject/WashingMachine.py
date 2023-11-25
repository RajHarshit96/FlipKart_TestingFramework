from selenium.webdriver.common.by import By


class TestWashingMachine:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    initialOption = (By.XPATH, "//div[.='Mobiles']")
    selectCatlog = (By.XPATH, "//span[.='TVs & Appliances']")
    selectIteamCatagoty = (By.XPATH, "//a[@title='Fully Automatic Front Load']")
    selectIteam = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[3]/div/div/div/a/div[2]/div[1]/div[1]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")

    # Function to be called in testCases
    def initialfirstOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWashingMachine.initialOption).click()

    def catlogSelect(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWashingMachine.selectCatlog)

    def IteamCatagorySelection(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWashingMachine.selectIteamCatagoty).click()

    def click_iteam(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWashingMachine.selectIteam).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*TestWashingMachine.selectIteam).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestWashingMachine.productVerifyMsg).text
        return msg






