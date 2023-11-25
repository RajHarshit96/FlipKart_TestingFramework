from selenium.webdriver.common.by import By


class test_Mobile:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    mobiles = (By.XPATH, "//div[.='Mobiles']")
    play = (By.XPATH, "//*[@id='container']/div/div[3]/div[7]/div/a/div/div/img[2]")

    gb = (By.XPATH, "//div[text()='Infinix HOT 12 Play (Daylight Green, 64 GB)']")
    crt = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button")

    # Function to be called in testCases
    def test_mobiles(self):
        return self.driver.find_element(*test_Mobile.mobiles).click()

    def test_play(self):
        return self.driver.find_element(*test_Mobile.play).click()

    def test_gb(self):
        return self.driver.find_element(*test_Mobile.gb).click()

    def test_crt(self):
        return self.driver.find_element(*test_Mobile.crt).click()
