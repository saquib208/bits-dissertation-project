import time
import random
from pageObject.BasePage import BasePage
from selenium.webdriver.support.ui import Select
from Locators.Locators import Locator as ele
from faker import Faker

class RegisterUser(BasePage):
    # Add customer Page
    fake = Faker()

    def __init__(self,driver):
        super().__init__(driver)

    def clickOnAdminMenu(self):
        self.wait_for_elemnt(ele.adminUser_xapth)
        self.do_click(ele.adminUser_xapth)

    def clickOnAddnewUser(self):
        self.wait_for_elemnt(ele.adNewUser_xpath)
        self.do_click(ele.adNewUser_xpath)

    def click_user_role_drpdn(self):
        self.wait_for_elemnt(ele.user_role_dropdown)
        self.do_click(ele.user_role_dropdown)

    def select_user(self):
        self.wait_for_elemnt(ele.selectList_xpath)
        self.select_second_value_from_drop_down_list(ele.selectList_xpath)

    def click_user_status_drop_down(self):
        self.wait_for_elemnt(ele.user_status_xpath)
        self.do_click(ele.user_status_xpath)

    def select_user_status_first_value(self):
        self.wait_for_elemnt(ele.user_status_xpath)
        self.select_first_value_from_drop_down_list(ele.user_status_xpath)

    def select_user_status_second_value(self):
        self.wait_for_elemnt(ele.user_status_xpath)
        self.select_second_value_from_drop_down_list(ele.user_status_xpath)

    def set_employee_name(self, emp_name=None):
        if emp_name == None:
            emp_name = self.fake.name()
            print("emp_name--->>" + emp_name)
            self.do_send_keys(ele.employee_name_xpath,emp_name)
        else:
            self.do_send_keys(ele.employee_name_xpath,emp_name)
        return emp_name

    def get_all_employee_record(self):
        emp_name = []
        for i in range(len(ele.employee_record)):

            elements = self.find_elements(ele.employee_record)
            emp_name.append(elements.text)
        print(emp_name)
        return emp_name

    def set_user_name(self, user_name=None):
        if user_name == None:
            user_name = self.fake.name()
            print("fname--->>" + user_name)
            self.do_send_keys(ele.username_xpath,user_name)
        else:
            self.do_send_keys(ele.username_xpath,user_name)
        return user_name

    def save_user(self):
        self.wait_for_elemnt(ele.save_xpath)
        self.do_click(ele.save_xpath)



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

    def set_user_password(self,password=None):
        if password == None:
            password = self.fake.password()
            print("Password-->>",password)
            self.do_send_keys(ele.input_password_xpath,password)
        else:
            self.do_send_keys(ele.input_password_xpath, password)
        return password

    def set_confirm_password(self,password=None):
        if password == None:
            password = self.fake.password()
            print("Password-->>",password)
            self.do_send_keys(ele.confirm_password_xpath,password)
        else:
            self.do_send_keys(ele.confirm_password_xpath, password)
        return password

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





