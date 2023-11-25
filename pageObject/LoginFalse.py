from selenium.webdriver.common.by import By


class TestLoginFal:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    hover = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div")
    logout = (By.XPATH, "//div[.='Logout']/..")

    userName = (By.XPATH, "//div[@class='_2MlkI1']/div/div[2]/div/form/div/input[@type='text']")
    Password = (By.XPATH, "//div[@class='_2MlkI1']/div/div[2]/div/form/div/input[@type='password']")
    submit = (By.XPATH, "//div[@class='_2MlkI1']/div/div[2]/div/form/div/button[@type='submit']")
    promt = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/span[3]/span")

    # Function to be called in testCases
    def qhover(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestLoginFal.hover)

    def qlogout(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestLoginFal.logout).click()

    def quserName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestLoginFal.userName)

    def qPassword(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestLoginFal.Password)

    def qsubmit(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestLoginFal.submit).click()

    def qpromt(self):
        self.driver.implicitly_wait(10)
        msg =  self.driver.find_element(*TestLoginFal.promt).text
        return msg