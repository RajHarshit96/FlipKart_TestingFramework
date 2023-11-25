from selenium.webdriver.common.by import By


class test_Round:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    travel = (By.XPATH, "//div[.='Travel']")
    full = (By.XPATH, "//*[@id='container']/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/label[2]/div[1]")
    search = (By.XPATH, "//*[@id='container']/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/button/span")
    change = (By.XPATH, "//*[@id='container']/div/div[2]/div/div[2]/div[1]/div/section[2]/div[2]/div[1]/label/div[1]")

    # Function to be called in testCases
    def test_travel(self):
        return self.driver.find_element(*test_Round.travel).click()

    def test_full(self):
        return self.driver.find_element(*test_Round.full).click()

    def test_search(self):
        return self.driver.find_element(*test_Round.search).click()

    def test_change(self):
        return self.driver.find_element(*test_Round.change).click()