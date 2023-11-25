from selenium.webdriver.common.by import By


class test_Router:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    electronic = (By.XPATH, "//div[.='Mobiles']")  # tuple
    hover = (By.XPATH, "//body/div[@id='container']/div[1]/div[2]/div[1]/div[1]/span[1]")
    rout = (By.XPATH, "//a[.='Routers']")
    product = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]")
    buy = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button")

    # Function to be called in testCases
    def test_items(self):
        return self.driver.find_element(*test_Router.electronic).click()  # calling by class name

    def test_hover(self):
        return self.driver.find_element(*test_Router.hover)  # for switching page

    def test_rout(self):
        return self.driver.find_element(*test_Router.rout)  # clicks in router

    def test_product(self):
        return self.driver.find_element(*test_Router.product).click()  # clicks in product

    def test_buy(self):
        return self.driver.find_element(*test_Router.buy).click()  # click on buy now
