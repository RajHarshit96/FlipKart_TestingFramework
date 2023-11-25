from selenium.webdriver.common.by import By


class TestHomef:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    initialOption = (By.XPATH, "//div[.='Mobiles']")
    hover = (By.XPATH, "//span[.='Home & Furniture']")
    selectIteamCatagoty = (By.XPATH, "//a[.='Bean Bags']")
    selectIteam = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[5]/div/div[1]/div/a[2]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")

    # Function to be called in testCases
    def initialfirstOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestHomef.initialOption).click()

    def qhover(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestHomef.hover)

    def IteamCatagorySelection(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestHomef.selectIteamCatagoty).click()

    def click_iteam(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestHomef.selectIteam).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*TestHomef.selectIteam).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestHomef.productVerifyMsg).text
        return msg
