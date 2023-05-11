import pytest
from Configuration.config import TestData
from pageObject.LoginPage import LoginPage
from pageObject.SearchEmployeePage import SearchEmployee
from pageObject.RegisterUserPage import RegisterUser
from testCase.test_Base import BaseTest
from Utility.customLogger import LogGen
import time

class Test_004_Search_Employee_Name(BaseTest):
    logger = LogGen.loggen()

    def test_search_employee(self):
        self.logger.info("***********TC_003 Add Customer Test***********")
        self.logger.info("****Started Add Customer Test****")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(TestData.USER_NAME)
        self.logger.info("****Enter Username****")
        self.loginPage.setPassword(TestData.PASSWORD)
        self.logger.info("****Enter Password****")
        self.loginPage.clickLogin()
        self.logger.info("****Click on Login Button****")

        self.addUser = RegisterUser(self.driver)
        self.addUser.clickOnAdminMenu()
        self.logger.info("****Click on User Menu Button****")

        self.searchEmp = SearchEmployee(self.driver)
        #print(self.searchEmp.getNumOfRows())
        user_name = self.searchEmp.return_all_user_name()
        employee_name = self.searchEmp.return_all_employee_name()



        time.sleep(15)


        # self.addCustomer.setEmail()
        # self.logger.info("**** Input Email ****")
        # self.addCustomer.setPassword()
        # self.logger.info("**** Input Password ****")
        # self.addCustomer.setFirstName()
        # self.logger.info("**** Input First Name****")
        # self.addCustomer.setLastName()
        # self.logger.info("**** Input Last Name****")
        # self.addCustomer.setGender()
        # self.logger.info("**** Input Gender ****")
        # self.addCustomer.setDob()
        # self.logger.info("**** Input DOB ****")
        # self.addCustomer.setCompanyName()
        # self.logger.info("**** Input Company Name ****")
        # self.addCustomer.setAdminContent()
        # self.logger.info("**** Input Admin Content ****")
        # self.addCustomer.clickOnSave()
        # self.logger.info("**** Customer Information Saved ****")
        # msg = self.addCustomer.get_customer_save_msg()
        # self.logger.info("customer validation msg-->>"+msg)
        # print("Message-->>"+msg[2:])
        # if msg[2:] in TestData.CUSTOMER_SAVE_MSG:
        #     assert True
        #     self.logger.info("********* Add customer Test Passed *********")
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")  # Screenshot
        #     self.logger.error("********* Add customer Test Failed ************")
        #     assert False

