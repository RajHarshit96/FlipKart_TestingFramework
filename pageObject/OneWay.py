from selenium.webdriver.common.by import By


class test_OneWay:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    travel = (By.XPATH, "//div[.='Travel']")
    way = (By.XPATH, "//div[.='One Way']/div")
    search = (By.XPATH, "//*[@id='container']/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/button/span")
    details = (By.XPATH, "//*[@id='container']/div/div[2]/div/div[2]/div[2]/div[3]/div/div[1]/div[3]/div[1]/div[2]/div[1]/span")
    book = (By.XPATH, "//*[@id='container']/div/div[2]/div/div[2]/div[2]/div[3]/div/div[1]/div[3]/div[1]/div[1]/div[4]")
    cont = (By.XPATH, "//div[.='CONTINUE']/div/div")
    select = (By.XPATH, "//*[@id='container']/div/div[2]/div/div[1]/div[3]/div[3]/form/div[1]/div/div[2]/div[1]/div/select")
    name = (By.XPATH, "//input[@name = 'First Name and Middle Name']")

    # Function to be called in testCases
    def test_travel(self):
        return self.driver.find_element(*test_OneWay.travel).click()

    def test_way(self):
        return self.driver.find_element(*test_OneWay.way).click()

    def test_search(self):
        return self.driver.find_element(*test_OneWay.search).click()

    def test_details(self):
        return self.driver.find_element(*test_OneWay.details).click()

    def test_book(self):
        return self.driver.find_element(*test_OneWay.book).click()

    def test_continue(self):
        return self.driver.find_element(*test_OneWay.cont).click()

    def test_drop(self):
        return self.driver.find_element(*test_OneWay.select).click()

    def test_name(self):
        return self.driver.find_element(*test_OneWay.name).send_keys("Ankit")
