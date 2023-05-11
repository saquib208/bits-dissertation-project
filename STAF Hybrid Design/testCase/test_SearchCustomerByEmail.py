import pytest
from Configuration.config import TestData
from pageObject.LoginPage import LoginPage
from pageObject.AddCustomerPage import AddCustomer
from pageObject.SearchCustomerPage import SearchCustomer
from testCase.test_Base import BaseTest
from Utility.customLogger import LogGen
import time

class Test_004_SerchCustomerByEmail(BaseTest):
    logger = LogGen.loggen()


    def test_search_customer_by_email(self):
        self.logger.info("***********TC_004 Search Customer By email Test***********")
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

        self.logger.info("******* Starting Search Customer By Email **********")

        self.searchCustomer = SearchCustomer(self.driver)

        self.logger.info("******* Entering Customer Email **********")
        Email = self.searchCustomer.search_email()
        print("Email-->>",Email)
        self.logger.info("******* Click on search Customer Email **********")
        self.searchCustomer.clickSearch()
        time.sleep(5)
        status = self.searchCustomer.verifyCustomerByEmail(Email)
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")

