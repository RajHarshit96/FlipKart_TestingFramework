from selenium.webdriver.common.by import By


class TestWomenTopOb:
    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    initialOption = (By.XPATH, "//div[.='Mobiles']")
    hover = (By.XPATH, "//span[.='Women']")
    selectIteamCatagoty = (By.XPATH, "//a[.='Topwear']")
    selectIteam = (By.XPATH, "//*[@id='container']/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/a[1]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]")

    # Function to be called in testCases
    def initialfirstOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWomenTopOb.initialOption).click()

    def qhover(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWomenTopOb.hover)

    def IteamCatagorySelection(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWomenTopOb.selectIteamCatagoty).click()

    def click_iteam(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWomenTopOb.selectIteam).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*TestWomenTopOb.selectIteam).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestWomenTopOb.productVerifyMsg).text
        return msg