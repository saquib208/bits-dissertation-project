import pytest
from Configuration.config import TestData
from pageObject.LoginPage import LoginPage
from pageObject.RegisterUserPage import RegisterUser
from pageObject.AddEmployee import AddEmployee
from testCase.test_Base import BaseTest
from pageObject.SearchEmployeePage import SearchEmployee
from Utility.customLogger import LogGen
import time


class Test_005_Add_Employee(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_user(self,setup):
        self.driver = setup
        self.logger.info("***********TC_005 Add Employee Test Case***********")
        self.logger.info("****Started Add Employee Test****")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(TestData.USER_NAME)
        self.logger.info("****Enter Username****")
        self.loginPage.setPassword(TestData.PASSWORD)
        self.logger.info("****Enter Password****")
        self.loginPage.clickLogin()
        self.logger.info("****Click on Login Button****")

        # self.addUser = RegisterUser(self.driver)
        # self.addUser.clickOnAdminMenu()
        # self.logger.info("****Click on User Menu Button****")

        self.addEmp = AddEmployee(self.driver)

        self.addEmp.clickOnPIM()
        self.logger.info("****Click on Add PIM  Button****")

        self.addEmp.clickOnAddnewEmp()
        self.logger.info("****Click on Add New Emp Button****")

        fname = self.addEmp.enter_emp_fname()
        self.logger.info("**** First Name Entered -->>"+fname+ "****")

        mName = self.addEmp.enter_emp_middle_name()
        self.logger.info("**** Middle Name Entered -->>" + mName + "****")

        lname = self.addEmp.enter_emp_lname()
        self.logger.info("**** Last Name Entered -->>" + lname + "****")
        time.sleep(5)
        self.addEmp.clickOnContactDetails()
        self.logger.info("****Click on Contact Details Button****")

        time.sleep(3)
        uname = self.addEmp.enter_username()
        self.logger.info("**** User Name Entered -->>" + uname + "****")


        password = self.addEmp.enter_password()
        self.logger.info("**** Password Entered -->>" + password + "****")


        self.addEmp.confirm_password(password)
        self.logger.info("**** Re-enter Password Entered -->>" + password + "****")


        self.addEmp.clickOnSaveBtn()
        self.logger.info("****Click on Save Button****")

        time.sleep(10)
        actual_empName = self.addEmp.verify_emp_name()
        print("Actual Emp Name",actual_empName)
        self.logger.info("***Actual Emp Name -->>" + actual_empName + "****")

        self.logger.info("**** Employee added Successfuly ****")
        time.sleep(5)
        if fname in actual_empName:
            assert True
            self.logger.info("*********Test Case Passed *********")
        else:
            #self.driver.save_screenshot(".\\Screenshots\\" + "test_addEmployee.png")  # Screenshot
            self.addEmp.get_screenshot("test_addEmp.png")
            self.logger.error("*********  Test Failed ************")
            assert False

        self.driver.close()



