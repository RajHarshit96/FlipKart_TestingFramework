from selenium.webdriver.common.by import By


class test_order:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    bar = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    click = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
    bottle = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]")
    atc = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button")
    place = (By.XPATH, "//span[.='Place Order']")

    # Function to be called in testCases
    def test_bar(self):
        return self.driver.find_element(*test_order.bar).send_keys("bottle")

    def test_click(self):
        return self.driver.find_element(*test_order.click).click()

    def test_bottle(self):
        return self.driver.find_element(*test_order.bottle).click()

    def test_addtocart(self):
        return self.driver.find_element(*test_order.atc).click()

    def test_place(self):
        return self.driver.find_element(*test_order.place).click()
