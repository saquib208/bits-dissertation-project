from selenium.webdriver.common.by import By


class Locator:
    #Login
    # textbox_username_id =(By.ID,"Email")
    # textbox_password_id = (By.ID, "Password")
    # button_login_xpath = (By.XPATH, "//*[@type='submit']")
    # link_logout_linktext = (By.LINK_TEXT, "Logout")

    textbox_username_id =(By.NAME,"username")
    textbox_password_id = (By.NAME, "password")
    button_login_xpath = (By.XPATH, "//*[@type='submit']")
    login_page_heading = (By.XPATH,"/*[@class='oxd-text oxd-text--h5 orangehrm-login-title']")
    home_page_heading = (By.XPATH,"//*[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    link_logout_linktext = (By.LINK_TEXT, "Logout")
    logout_dropdown_xpath = (By.XPATH,"//*[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")

    #Add User
    adminUser_xapth = (By.XPATH,"//*[@href='/web/index.php/admin/viewAdminModule']")
    adNewUser_xpath = (By.XPATH,"//*[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    user_role_dropdown = (By.XPATH,"//*[text()='User Role']//following::div[@class='oxd-select-text--after'][1]")
    selectList_xpath = (By.XPATH,"//*[@role='listbox']")
    optionBox_xapth = (By.XPATH,"//*[@class='oxfd-select-option']")
    user_status_xpath = (By.XPATH,"//*[text()='User Role']//following::div[@class='oxd-select-text--after'][2]")
    input_password_xpath = (By.XPATH,"//*[text()='Password']//following::input[1]")
    confirm_password_xpath = (By.XPATH, "//*[text()='Confirm Password']//following::input[@class='oxd-input oxd-input--active']")
    employee_name_xpath = (By.XPATH,"//*[@placeholder='Type for hints...']")
    username_xpath = (By.XPATH,"//*[text()='Username']//following::input[1]")
    save_xpath =(By.XPATH,"//*[@type='submit']")

    #List Employee
    employee_record = (By.XPATH,"//*[@class='oxd-table-cell oxd-padding-cell' and @role='cell'][4]")

    #Search Employee
    searchUsername_Xpath = (By.XPATH,"//*[text()='Username']//following::input[@class='oxd-input oxd-input--active']")

    #Add Employee
    personalInfo_Xpath =(By.XPATH,"//*[@href='/web/index.php/pim/viewPimModule']")
    addEmp_xpath =(By.XPATH, "//*[@class='oxd-topbar-body-nav-tab --visited']//a")
    empFirstName_Xpath =(By.XPATH, "//*[@name='firstName']")
    empMiddleName_Xpath =(By.XPATH, "//*[@name='middleName']")
    empLastName_Xpath = (By.XPATH,"//*[@name='lastName']")
    createLoginButton_Xapth = (By.XPATH,"//*[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    Empusername_Xpath = (By.XPATH,"//*[text()='Username']//following::input[@class='oxd-input oxd-input--active'][1]")
    password_Xpath = (By.XPATH,"//*[text()='Password']//following::input[@class='oxd-input oxd-input--active'][1]")
    confirmPass_Xpath = (By.XPATH,"//*[text()='Password']//following::input[@class='oxd-input oxd-input--active'][2]")
    saveBtn_Xapth = (By.XPATH,"//*[@type='submit']")
    empName_Xpath = (By.XPATH,"//*[@class='orangehrm-edit-employee-name']//h6")


    #Add Customer
    lnkCustomers_menu_xpath =  (By.XPATH,"//*[@href='#']//*[contains(text(),'Customers')]")
    lnkCustomers_menuitem_xpath = (By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    btnAddnew_xpath = (By.CSS_SELECTOR,"a[class='btn btn-primary']")
    txtEmail_xpath = (By.XPATH,"//input[@id='Email']")
    txtPassword_xpath = (By.XPATH,"//input[@id='Password']")
    txtFirstName_xpath = (By.XPATH,"//input[@id='FirstName']")
    txtLastName_xpath = (By.XPATH,"//input[@id='LastName']")
    rdMaleGender_id = (By.ID,"Gender_Male")
    txtDob_xpath = (By.XPATH, "//input[@id='DateOfBirth']")
    rdFeMaleGender_id = (By.ID, "Gender_Female")
    txtCompanyName_xpath = (By.XPATH,"//input[@id='Company']")
    txtAdminContent_xpath = (By.XPATH,"//textarea[@id='AdminComment']")
    btnSave_xpath = (By.XPATH,"//button[@name='save']")
    custome_validation_css = (By.XPATH,"//*[@class='alert alert-success alert-dismissable']")
    txtcustomerRoles_xpath = (By.XPATH,"//div[@class='k-multiselect-wrap k-floatwrap']")
    lstitemAdministrators_xpath = (By.XPATH,"//li[contains(text(),'Administrators')]")
    lstitemRegistered_xpath = (By.PARTIAL_LINK_TEXT,"//li[contains(text(),'Registered')]")
    lstitemGuests_xpath = (By.XPATH,"//li[contains(text(),'Guests')]")
    lstitemVendors_xpath = (By.XPATH,"//li[contains(text(),'Vendors')]")
    drpmgrOfVendor_xpath = (By.XPATH,"//*[@id='VendorId']")


    #Search Customer

    txtEmail_id = (By.ID,"SearchEmail")
    txtFirstName_id= (By.ID,"SearchFirstName")
    txtLastName_id=(By.ID,"SearchLastName")
    btnSearch_id=(By.XPATH,"//*[@id='search-customers']")
    tblSearchResults_xpath=(By.XPATH,"//table[@role='grid']")
    table_xpath=(By.XPATH,"//table[@id='customers-grid']")
    tableRows_xpath=(By.XPATH,"//table[@id='customers-grid']//tbody/tr")
    tableColumns_xpath=(By.XPATH,"//table[@id='customers-grid']//tbody/tr/td")



