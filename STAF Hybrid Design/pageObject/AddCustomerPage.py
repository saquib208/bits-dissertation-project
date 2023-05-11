import time
import random
from pageObject.BasePage import BasePage
from selenium.webdriver.support.ui import Select
from Locators.Locators import Locator as ele
from faker import Faker

class AddCustomer(BasePage):
    # Add customer Page
    fake = Faker()

    def __init__(self,driver):
        super().__init__(driver)

    def clickOnCustomersMenu(self):
        self.wait_for_elemnt(ele.lnkCustomers_menu_xpath)
        self.do_click(ele.lnkCustomers_menu_xpath)

    def clickOnCustomersMenuItem(self):
        self.wait_for_elemnt(ele.lnkCustomers_menuitem_xpath)
        self.do_click(ele.lnkCustomers_menuitem_xpath)

    def clickOnAddnew(self):
        self.wait_for_elemnt(ele.btnAddnew_xpath)
        self.do_click(ele.btnAddnew_xpath)

    def setEmail(self,email=None):
        if email == None:
            email = self.fake.email()
            print("Email--->>"+email)
            self.do_send_keys(ele.txtEmail_xpath,email)
        else:
            self.do_send_keys(ele.txtEmail_xpath,email)

    def setFirstName(self, fname=None):
        if fname == None:
            fname = self.fake.name()
            print("fname--->>" + fname)
            self.do_send_keys(ele.txtFirstName_xpath,fname)
        else:
            self.do_send_keys(ele.txtFirstName_xpath,fname)

    def setLastName(self, lname=None):
        if lname == None:
            lname=self.fake.name()
            print("lname--->>" + lname)
            self.do_send_keys(ele.txtLastName_xpath,lname)
        else:
            self.do_send_keys(ele.txtLastName_xpath,lname)

    def setPassword(self,password=None):
        if password == None:
            password = self.fake.password()
            self.do_send_keys(ele.txtPassword_xpath,password)
        else:
            self.do_send_keys(ele.txtPassword_xpath, password)

    def setDob(self, dob=None):
        if dob == None:
            dob=self.fake.date()
            print("dob--->>" + dob)
            self.do_send_keys(ele.txtDob_xpath,dob)
        else:
            self.do_send_keys(ele.txtDob_xpath, dob)

    def setGender(self, gen=None):
        gender = random.choice(['Male', 'Female'])
        if gender == 'Male':
            self.do_click(ele.rdMaleGender_id)
        elif gender == 'Female':
            self.do_click(ele.rdFeMaleGender_id)
        else:
            self.do_click(ele.rdMaleGender_id)

    def setCompanyName(self, comname=None):
        if comname == None:
            comname=self.fake.name()
            print("Company Name--->>" + comname)
            self.do_send_keys(ele.txtCompanyName_xpath,comname)
        else:
            self.do_send_keys(ele.txtCompanyName_xpath,comname)


    def setAdminContent(self, content=None):
        if content == None:
            content = self.fake.text()
            print("Admin Content--->>" + content)
            self.do_send_keys(ele.txtAdminContent_xpath,content)
        else:
            self.do_send_keys(ele.txtAdminContent_xpath, content)

    def clickOnSave(self):
        self.do_click(ele.btnSave_xpath)

    def get_customer_save_msg(self):
        msg = self.get_element_text(ele.custome_validation_css)
        print("Validation Message-->>"+msg)
        return msg

    def setCustomerRoles(self,role):
        self.do_click(ele.txtcustomerRoles_xpath)
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.find_element(ele.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.find_element(ele.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.do_click("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]")
            self.listitem = self.find_element(ele.lstitemGuests_xpath)
        elif role=='Registered':
            self.listitem = self.find_element(ele.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.find_element(ele.lstitemVendors_xpath)
        else:
            self.listitem = self.find_element(ele.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.find_element(ele.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)





