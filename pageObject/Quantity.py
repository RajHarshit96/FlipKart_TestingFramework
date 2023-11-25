from selenium.webdriver.common.by import By


class test_quant:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    bar = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    click = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
    aeroplane = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]")

    cart = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button")
    clean = (By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/input")

    # Function to be called in testCases
    def test_bar(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*test_quant.bar).send_keys("aeroplane")

    def test_click(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*test_quant.click).click()

    def test_aero(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*test_quant.aeroplane).click()

    def test_cart(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*test_quant.cart).click()

    def test_clear(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*test_quant.clean).clear()
        return self.driver.find_element(*test_quant.clean).send_keys("2")

    def scroll(self):
        self.driver.implicitly_wait(10)
        return self.driver.execute_script("window.scrollBy(0,3000)","")
