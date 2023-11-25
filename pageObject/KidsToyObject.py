from selenium.webdriver.common.by import By


class TestToys:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    startOption = (By.XPATH, "//div[.='Mobiles']")
    kidsCatlog = (By.XPATH, "//span[.='Baby & Kids']")
    selCatagory = (By.XPATH, "//a[.='Remote Control Toys']")
    selectItm = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/a[2]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")

    # Function to be called in testCases
    def qstartOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestToys.startOption).click()

    def qkidsCatlog(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestToys.kidsCatlog)

    def qselCatagory(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestToys.selCatagory).click()

    def qselectItm(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestToys.selectItm).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*TestToys.selectItm).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestToys.productVerifyMsg).text
        return msg