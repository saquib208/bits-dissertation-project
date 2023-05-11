import pytest
from Configuration.config import TestData
from pageObject.LoginPage import LoginPage
from pageObject.AddCustomerPage import AddCustomer
from pageObject.SearchCustomerPage import SearchCustomer
from testCase.test_Base import BaseTest
from Utility.customLogger import LogGen
import time

class Test_SearchCustomerByName_005(BaseTest):
    logger = LogGen.loggen()


    def test_search_customer_by_name(self):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.logger.info("****Started Search Customer By email Test****")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(TestData.USER_NAME)
        self.logger.info("****Enter Username****")
        self.loginPage.setPassword(TestData.PASSWORD)
        self.logger.info("****Enter Password****")
        self.loginPage.clickLogin()
        self.logger.info("****Click on Login Button****")
        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.clickOnCustomersMenu()
        self.logger.info("****Click on Customer Menu Button****")
        self.addCustomer.clickOnCustomersMenuItem()
        self.logger.info("****Click on Menu Item Button****")
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.searchCustomer = SearchCustomer(self.driver)

        self.logger.info("******* Entering Customer Name **********")
        name = self.searchCustomer.search_by_fname()
        print("Name-->>",name)
        self.logger.info("******* Click on search Customer Name **********")
        self.searchCustomer.clickSearch()
        time.sleep(5)
        status = self.searchCustomer.verifyCustomerByName(name)
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_005 Finished  *********** ")

