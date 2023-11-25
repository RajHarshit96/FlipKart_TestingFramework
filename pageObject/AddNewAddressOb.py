from selenium.webdriver.common.by import By


class TestAddAddressOb:

    def __init__(self, driver):
        self.driver = driver

    # Locators Are Assigned to Variable

    hover = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div")
    myProfile = (By.XPATH, "//div[.='My Profile']")
    whover = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
    manageAdd = (By.XPATH, "//div[.='Manage Addresses']")
    addNewAdd = (By.XPATH, "//*[@id='container']/div/div[3]/div/div[2]/div/div/div/div[1]/div/div")
    saveBtn = (By.XPATH, "//*[@id='container']/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[8]/button[1]")

    # Locators of Form for New Address
    dropDLoc = (By.NAME, "state")
    name = (By.NAME, "name")
    phone = (By.NAME, "phone")
    pincode = (By.NAME, "pincode")
    address2 = (By.NAME, "addressLine2")
    address1 = (By.NAME, "addressLine1")
    landmark = (By.NAME, "landmark")
    radioBtn = (By.XPATH, "//div[@class='_1XFPmK']")


    # Function to be called in testCases
    def qhover(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.hover)

    def qMyProfile(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.myProfile).click()

    def qWhover(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.whover)

    def qmanageAdd(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.manageAdd).click()

    def qAddNewAddd(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.addNewAdd).click()

    def qname(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.name)

    def qPhone(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.phone)

    def qPincode(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.pincode)

    def qAddress2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.address2)

    def qAddress1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.address1)

    def qLandmark(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.landmark)

    def qRadioBtn(self):
        self.driver.implicitly_wait(10)
        radios = self.driver.find_elements(*TestAddAddressOb.radioBtn)
        return radios[1].click()

    def qSaveBtn(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.saveBtn).click()

    def qDropDLOC(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(*TestAddAddressOb.dropDLoc)
