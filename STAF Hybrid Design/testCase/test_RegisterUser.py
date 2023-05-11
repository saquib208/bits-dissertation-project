import pytest
from Configuration.config import TestData
from pageObject.LoginPage import LoginPage
from pageObject.RegisterUserPage import RegisterUser
from testCase.test_Base import BaseTest
from pageObject.SearchEmployeePage import SearchEmployee
from Utility.customLogger import LogGen
import time
import allure


class Test_003_Add_User(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_user(self,setup):
        self.driver = setup
        self.logger.info("***********TC_003 Register CRM User Test Case***********")
        self.logger.info("****Started Register User Test****")
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
        self.addUser.clickOnAddnewUser()
        self.logger.info("****Click on Add New USer Button****")
        self.addUser.click_user_role_drpdn()
        time.sleep(2)
        self.logger.info("**** Click User Role Drop Down****")
        self.addUser.select_user()

        self.logger.info("**** Role selected from drop down list ****")

        password = self.addUser.set_user_password()
        self.logger.info("**** Password Entered -->>"+password+ "****")

        self.addUser.set_employee_name("a")
        time.sleep(2)
        self.addUser.select_user()
        self.logger.info("**** Employee Name Entered ****")
        time.sleep(2)
        user_name = self.addUser.set_user_name()
        self.logger.info("**** Username Entered-->>"+user_name+ "****")

        self.addUser.click_user_status_drop_down()
        self.logger.info("**** Click on User Status drop down list ****")
        time.sleep(2)
        self.addUser.select_user_status_second_value()
        self.logger.info("**** Select User Status from drop down list ****")

        time.sleep(2)
        self.addUser.set_confirm_password(password)
        self.logger.info("**** Confirm Password Entered ****")
        time.sleep(2)

        self.addUser.save_user()
        self.logger.info("**** User added Successfuly ****")
        time.sleep(5)
        self.searchEmp = SearchEmployee(self.driver)

        actual_user_name = self.searchEmp.return_all_user_name()
        if user_name in actual_user_name:
            assert True
            self.logger.info("********* Register CRM User Test Case Passed *********")
        else:
            #self.driver.save_screenshot(".\\Screenshots\\" + "test_Register.png")  # Screenshot
            self.addUser.get_screenshot("test_Register.png")
            self.logger.error("********* Register User Test Failed ************")
            assert False

        self.driver.close()



