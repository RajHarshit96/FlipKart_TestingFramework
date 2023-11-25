from selenium.webdriver.common.by import By


class TestSchoolSuppliesOb:
    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    startOption = (By.XPATH, "//div[.='Mobiles']")
    kidsCatlog = (By.XPATH, "//span[.='Baby & Kids']")
    selCatagory = (By.XPATH, "//a[.='School Bags']")
    selectItm = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/a[2]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")

    # Function to be called in testCases
    def qstartOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestSchoolSuppliesOb.startOption).click()

    def qkidsCatlog(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestSchoolSuppliesOb.kidsCatlog)

    def qselCatagory(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestSchoolSuppliesOb.selCatagory).click()

    def qselectItm(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestSchoolSuppliesOb.selectItm).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*TestSchoolSuppliesOb.selectItm).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestSchoolSuppliesOb.productVerifyMsg).text
        return msg