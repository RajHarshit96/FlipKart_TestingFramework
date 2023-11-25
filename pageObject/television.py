from selenium.webdriver.common.by import By


class TestTelevision:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    OptionClick = (By.XPATH, "//div[.='Mobiles']")
    hoverOption = (By.XPATH, "//span[.='TVs & Appliances']")
    clickTV = (By.XPATH, "//a[@title='Television']")
    selectProduct = (By.XPATH, "//*[@id='container']/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div/div[1]/div[1]/a")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")

    # Function to be called in testCases
    def optionOne(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestTelevision.OptionClick).click()

    def hover(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestTelevision.hoverOption)

    def click_tv(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestTelevision.clickTV)

    def getText(self):
        self.driver.implicitly_wait(10)
        word =  self.driver.find_element(*TestTelevision.selectProduct).text
        text = ' '.join(word.split()[:3])
        return text

    def selectPRODUCT(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestTelevision.selectProduct).click()

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestTelevision.productVerifyMsg).text
        return msg
