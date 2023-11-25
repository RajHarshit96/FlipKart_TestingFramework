from selenium.webdriver.common.by import By


class TestOrder_Product:
    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    searchBar = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    clickSearch =(By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
    findProduct = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]")
    buyButton = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button")
    deliverBtn = (By.XPATH, "//button[.='Deliver Here']")
    continuePayment = (By.XPATH, "//span[@id='to-payment']/button")

    # Function to be called in testCases
    def searchIteam(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestOrder_Product.searchBar).send_keys("Metier Bong")

    def clickToSearch(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestOrder_Product.clickSearch).click()

    def lookForProduct(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestOrder_Product.findProduct).click()

    def clickBuynow(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestOrder_Product.buyButton).click()

    def selectAddress(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestOrder_Product.deliverBtn).click()

    def goToPayment(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestOrder_Product.continuePayment).click()

    def acceptCondition(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestOrder_Product.acceptTerm).click()
