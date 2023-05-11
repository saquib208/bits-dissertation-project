import time
import random
from pageObject.BasePage import BasePage
from selenium.webdriver.support.ui import Select
from Locators.Locators import Locator as ele
from faker import Faker

class AddEmployee(BasePage):
    # Add Employee Page
    fake = Faker()

    def __init__(self,driver):
        super().__init__(driver)


    def clickOnPIM(self):
        self.wait_for_elemnt(ele.personalInfo_Xpath)
        self.do_click(ele.personalInfo_Xpath)

    def clickOnAddnewEmp(self):
        self.wait_for_elemnt(ele.adNewUser_xpath)
        self.do_click(ele.adNewUser_xpath)


    def enter_emp_fname(self, emp_name=None):
        if emp_name == None:
            emp_name = self.fake.first_name()
            print("emp_name--->>" + emp_name)
            self.do_send_keys(ele.empFirstName_Xpath,emp_name)
        else:
            self.do_send_keys(ele.empFirstName_Xpath,emp_name)
        return emp_name

    def enter_emp_middle_name(self, emp_name=None):
        if emp_name == None:
            emp_name = self.fake.last_name()
            print("emp_name--->>" + emp_name)
            self.do_send_keys(ele.empMiddleName_Xpath,emp_name)
        else:
            self.do_send_keys(ele.empMiddleName_Xpath,emp_name)
        return emp_name

    def enter_emp_lname(self, emp_name=None):
        if emp_name == None:
            emp_name = self.fake.last_name()
            print("emp_name--->>" + emp_name)
            self.do_send_keys(ele.empLastName_Xpath,emp_name)
        else:
            self.do_send_keys(ele.empLastName_Xpath,emp_name)
        return emp_name

    def enter_username(self, user_name=None):
        if user_name == None:
            user_name = self.fake.first_name()
            print("user_name--->>" + user_name)
            self.do_send_keys(ele.Empusername_Xpath,user_name)
        else:
            self.do_send_keys(ele.Empusername_Xpath,user_name)
        return user_name

    def enter_password(self, password=None):
        if password == None:
            password = self.fake.password()
            print("passowrd--->>" + password)
            self.do_send_keys(ele.password_Xpath,password)
        else:
            self.do_send_keys(ele.password_Xpath,password)
        return password

    def confirm_password(self, password):
        self.do_send_keys(ele.confirm_password_xpath,password)
        return password


    def clickOnContactDetails(self):
        self.wait_for_elemnt(ele.createLoginButton_Xapth)
        self.do_click(ele.createLoginButton_Xapth)

    def clickOnSaveBtn(self):
        self.wait_for_elemnt(ele.saveBtn_Xapth)
        self.do_click(ele.saveBtn_Xapth)

    def verify_emp_name(self):
        self.wait_for_elemnt(ele.empName_Xpath)
        emp_name = self.find_element(ele.empName_Xpath).text
        print("Actual Emp Name From Web-->>"+emp_name)
        return emp_name