from selenium.webdriver.common.by import By


class test_search:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    sbar = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    click = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
    jeans = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/div/a[1]")
    size = (By.XPATH, "//a[.=32]")
    cart = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]")

    # Function to be called in testCases
    def test_sbar(self):
        return self.driver.find_element(*test_search.sbar).send_keys("jeans women")

    def test_click(self):
        return self.driver.find_element(*test_search.click).click()

    def test_jeans(self):
        return self.driver.find_element(*test_search.jeans).click()

    def test_size(self):
        return  self.driver.find_element(*test_search.size).click()

    def test_cart(self):
        return self.driver.find_element(*test_search.cart).click()

    def scroll(self):
        return self.driver.execute_script("window.scrollBy(0,2270)","")

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*test_search.jeans).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*test_search.productVerifyMsg).text
        return msg