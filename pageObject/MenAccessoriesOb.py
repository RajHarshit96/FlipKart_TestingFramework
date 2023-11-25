from selenium.webdriver.common.by import By


class TestMenAccessoriesOb:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    startOption = (By.XPATH, "//div[.='Mobiles']")
    hoverOn = (By.XPATH, "//span[.='Men']")
    catogory = (By.XPATH, "//a[.='Wallets']")
    selectItm = (By.XPATH, "//*[@id='container']/div/div[3]/div/div[2]/div[2]/div/div[3]/div/div/a[1]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]")

    # Function to be called in testCases
    def qstartOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestMenAccessoriesOb.startOption).click()

    def qhaverOn(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestMenAccessoriesOb.hoverOn)

    def qcatogory(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestMenAccessoriesOb.catogory).click()

    def qselectItm(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestMenAccessoriesOb.selectItm).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*TestMenAccessoriesOb.selectItm).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestMenAccessoriesOb.productVerifyMsg).text
        return msg