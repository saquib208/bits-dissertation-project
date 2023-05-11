from selenium.webdriver.common.by import By
from Locators.Locators import Locator as ele
from Configuration.config import TestData
from pageObject.BasePage import BasePage
from pageObject.HomePage import HomePage
import time
from Utility.customLogger import LogGen

class LoginPage(BasePage):
    logger = LogGen.loggen()

    def __init__(self,driver):
        super().__init__(driver)
        time.sleep(5)
        self.driver.get(TestData.BASE_URL)

    def naviagate_to_login_page(self):
        self.driver.get(TestData.AUTH_URL)

    def setUserName(self, username):
        self.do_clear(ele.textbox_username_id)
        self.do_send_keys(ele.textbox_username_id, username)

    def setPassword(self, password):
        self.do_clear(ele.textbox_password_id)
        self.do_send_keys(ele.textbox_password_id, password)

    def clickLogin(self):
        self.do_click(ele.button_login_xpath)

    def clickLogout(self):
        self.do_click(ele.logout_dropdown_xpath)
        self.do_click(ele.link_logout_linktext)

    def get_login_page_title(self,title):
        return self.get_title(title)

    def get_login_page_heading(self):
        login_heading = self.find_element(ele.login_page_heading).text
        self.logger.info("Login Page Heading-->>"+login_heading)
        return login_heading

    def get_home_page_heading(self):
        home_page_haeding = self.find_element(ele.home_page_heading).text
        self.logger.info("Home Page Heading-->>"+home_page_haeding)
        return home_page_haeding

    def is_sign_up_link_exists(self,SIGNUP_LINK):
        return self.is_visible(SIGNUP_LINK)

    def do_login(self,username,password):
        self.do_clear(ele.textbox_username_id)
        self.do_send_keys(ele.textbox_username_id,username)
        self.do_clear(ele.textbox_password_id)
        self.do_send_keys(ele.textbox_password_id,password)
        self.do_click(ele.button_login_xpath)
        return HomePage(self.driver)


