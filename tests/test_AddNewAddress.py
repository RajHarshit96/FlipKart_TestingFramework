import time

import pytest
from selenium.webdriver import ActionChains

from TestData.AddNewAddressDATA import AddNewAddresssData
from pageObject.AddNewAddressOb import TestAddAddressOb
from utilities.BaseClass import BaseClass


class TestAddNewAdd(BaseClass):

    def test_NewAddress(self, getData):
        log = self.getLogger()
        newAdd = TestAddAddressOb(self.driver)

        self.hover(newAdd.qhover())
        log.info("Going to Click on Profile")
        newAdd.qMyProfile()

        self.hover(newAdd.qWhover())

        time.sleep(4)
        newAdd.qmanageAdd()
        log.info("Manage Address Opened")
        time.sleep(3)

        newAdd.qAddNewAddd()
        newAdd.qname().send_keys(getData["name"])
        log.info("Name entered as " + getData["name"])

        newAdd.qPhone().send_keys(getData["phone"])
        log.info("Phone No. entered "+ getData["phone"])

        newAdd.qPincode().send_keys(getData["pincode"])
        log.info("Pincode entered as " + getData["pincode"])

        newAdd.qAddress2().send_keys(getData["addressLine2"])
        log.info("Address2 entered")

        newAdd.qAddress1().send_keys(getData["addressLine1"])
        log.info("Address1 entered")

        newAdd.qLandmark().send_keys(getData["landmark"])
        log.info("Landmark entered as "+ getData["landmark"])


        self.selectOptionByText(newAdd.qDropDLOC(), getData["visibleText"])
        log.info("State selected as"+ getData["visibleText"])

        newAdd.qRadioBtn()
        log.info("Radio button is selected")

        newAdd.qSaveBtn()
        log.info("Save button click")

        log.info("<<<<<<<NEW TEST CASE IS STARTING>>>>>>>")


    @pytest.fixture(params=AddNewAddresssData.test_AddNewAddress_data)
    def getData(self, request):
        return request.param