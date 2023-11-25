from selenium.webdriver.common.by import By


class test_HomePage:

    def __init__(self, driver):  # defined constructor accepting driver
        self.driver = driver

    # Locators Are Assigned to Variable
    electronic = (By.XPATH, "//div[contains(text(),'Mobiles')]")  # tuple
    hover = (By.XPATH, "//body/div[@id='container']/div[1]/div[2]/div[1]/div[1]/span[1]")
    watch = (By.XPATH, "//a[.='Smart Bands']")
    apple = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[4]/div/div/div/a/div[2]/div[1]/div[1]")
    buy = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button")

    # Function to be called in testCases
    def test_shopItems(self):
        return self.driver.find_element(*test_HomePage.electronic).click()  # calling by class name

    def test_hover(self):
        return self.driver.find_element(*test_HomePage.hover)  # for switching page

    def test_watch(self):
        return self.driver.find_element(*test_HomePage.watch)  # click smart watch

    def test_apple(self):
        return self.driver.find_element(*test_HomePage.apple).click()   # clicks on apple watch

    def test_buyNow(self):
        return self.driver.find_element(*test_HomePage.buy).click()    # click on buy now
