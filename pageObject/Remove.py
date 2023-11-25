from selenium.webdriver.common.by import By


class test_removes:

    def __init__(self,driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    cart = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[6]/div/div/a/span")
    remove = (By.XPATH, "//div[.='Remove']")
    remitem = (By.XPATH, "//*[@id='container']/div/div[1]/div/div[3]/div/div[2]")

    # Function to be called in testCases
    def test_cart(self):
        return self.driver.find_element(*test_removes.cart).click()

    def test_remove(self):
        return self.driver.find_element(*test_removes.remove).click()

    def test_item(self):
        return self.driver.find_element(*test_removes.remitem).click()