from selenium.webdriver.common.by import By


class TestMenFootOb:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable
    startOption = (By.XPATH, "//div[.='Mobiles']")
    kidsCatlog = (By.XPATH, "//span[.='Men']")
    qIteamCatagory = (By.XPATH, "//a[.='Formal Shoes']")
    seletIteam = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[3]/div/div[3]/div/div/a[1]")
    productVerifyMsg = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]")

    # Function to be called in testCases
    def qstartOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestMenFootOb.startOption).click()


    def qkidsCatlog(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestMenFootOb.kidsCatlog)


    def qqIteamCatagory(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestMenFootOb.qIteamCatagory).click()


    def qqseletIteam(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestMenFootOb.seletIteam).click()

    def getText(self):
        self.driver.implicitly_wait(10)
        word = self.driver.find_element(*TestMenFootOb.seletIteam).text
        text = ' '.join(word.split()[:3])
        return text

    def productNameVerify(self):
        self.driver.implicitly_wait(10)
        msg = self.driver.find_element(*TestMenFootOb.productVerifyMsg).text
        return msg