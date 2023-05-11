import time
import random
from pageObject.BasePage import BasePage
from selenium.webdriver.support.ui import Select
from Locators.Locators import Locator as ele
from selenium.webdriver.common.by import By



class SearchEmployee(BasePage):
    # Add customer Page
    userName_xpath = (By.XPATH, "//*[@class='oxd-table-cell oxd-padding-cell' and @role='cell'][2]")
    empName_xpath = (By.XPATH, "//*[@class='oxd-table-cell oxd-padding-cell' and @role='cell'][4]")

    def __init__(self,driver):
        super().__init__(driver)

    def getNumOfRows(self):
        self.wait_for_elemnt(self.userName_xpath)
        no_of_rows = self.find_elements(self.userName_xpath)
        print(no_of_rows)
        return len(no_of_rows)

    def return_all_user_name(self):
        user_name =[]
        self.wait_for_elemnt(self.userName_xpath)
        names = self.find_elements(self.userName_xpath)
        for i in names:
            name = i.text
            user_name.append(name)
        print(user_name)
        return user_name

    def return_all_employee_name(self):
        employee_name =[]
        self.wait_for_elemnt(self.empName_xpath)
        names = self.find_elements(self.empName_xpath)
        for j in names:
            name = j.text
            employee_name.append(name)
        print(employee_name)
        return employee_name

    def clickOnAddnewUser(self):
        self.wait_for_elemnt(ele.adNewUser_xpath)
        self.do_click(ele.adNewUser_xpath)