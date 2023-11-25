from selenium.webdriver.common.by import By


class test_wish:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    sb = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    cli = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
    x = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/a[1]/div[1]/div/div/img")
    wish = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[1]/div/div[2]")
    eh = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[1]/div/div[2]")

    # Function to be called in testCases
    def test_sb(self):
        return self.driver.find_element(*test_wish.sb).send_keys("beatuy blender")

    def test_click(self):
        return self.driver.find_element(*test_wish.cli).click()

    def test_x(self):
        return self.driver.find_element(*test_wish.x).click()

    def test_ish(self):
        return self.driver.find_element(*test_wish.wish).click()

    def test_eh(self):
        return self.driver.find_element(*test_wish.eh).click()
