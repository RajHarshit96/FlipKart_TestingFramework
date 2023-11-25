from selenium.webdriver.common.by import By


class TestWomenHandBagOb:
    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    initialOption = (By.XPATH, "//div[.='Mobiles']")
    hover = (By.XPATH, "//span[.='Women']")
    selectIteamCatagoty = (By.XPATH, "//a[.='Handbags']")

    # Select Iteam
    selectIteam = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/div/a[1]")

    # Verify the product Text
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]")

    # Function to be called in testCases
    def initialfirstOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWomenHandBagOb.initialOption).click()

    def qhover(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWomenHandBagOb.hover)

    def IteamCatagorySelection(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWomenHandBagOb.selectIteamCatagoty).click()

    def click_iteam(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestWomenHandBagOb.selectIteam).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*TestWomenHandBagOb.selectIteam).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestWomenHandBagOb.productVerifyMsg).text
        return msg