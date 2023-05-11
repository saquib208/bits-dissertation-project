import time
import random
from pageObject.BasePage import BasePage
from selenium.webdriver.support.ui import Select
from Locators.Locators import Locator as ele
from faker import Faker
from selenium.webdriver.common.by import By

class SearchCustomer(BasePage):
    # Add customer Page

    email_list = ["arthur_holmes@nopCommerce.com","brenda_lindgren@nopCommerce.com","steve_gates@nopCommerce.com","victoria_victoria@nopCommerce.com"]
    fname_list = ["Brenda","Arthur","John","Victoria"]
    lname_list = ["Lindgren", "Holmes", "Smith","Terces"]



    def __init__(self,driver):
        super().__init__(driver)

    def search_email(self,email=None):
        email = random.choice(self.email_list)
        self.do_clear(ele.txtEmail_id)
        self.do_send_keys(ele.txtEmail_id,email)
        return email

    def search_by_fname(self,fname=None):
        fname = random.choice(self.fname_list)
        self.do_clear(ele.txtFirstName_id)
        self.do_send_keys(ele.txtFirstName_id,fname)
        return fname

    def search_by_lname(self,lname=None):
        lname = random.choice(self.lname_list)
        self.do_clear(ele.txtLastName_id)
        self.do_send_keys(ele.txtLastName_id,lname)
        return lname

    def clickSearch(self):
        self.do_click(ele.btnSearch_id)

    def getNoOfRows(self):
        no_of_rows = len(self.find_elements(ele.tableRows_xpath))
        print("No of rows-->>",no_of_rows)
        return no_of_rows

    def getNoOfColumns(self):
        no_of_columns = len(self.find_elements(ele.tableColumns_xpath))
        return no_of_columns

    def verifyCustomerByEmail(self,email):
        print("Email ID to verify-->>",email)
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          #table=self.find_element(ele.table_xpath)
          dynamic_xpath = "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]"
          print(dynamic_xpath)
          table_locator = (By.XPATH,dynamic_xpath)

          emailid=self.driver.find_element(*table_locator).text
          print("Email ID from the Web Page-->>",emailid)
          if emailid == email:
              flag = True
        return flag

    def verifyCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          dynamic_xpath = "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]"
          print(dynamic_xpath)
          table_locator = (By.XPATH,dynamic_xpath)
          name=self.driver.find_element(*table_locator).text
          print("Name  from the Web Page-->>",name)
          if name == Name:
              flag = True
              break
        return flag


