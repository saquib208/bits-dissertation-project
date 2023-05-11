import pytest
from allure_commons.types import AttachmentType

from Configuration.config import TestData
from pageObject.LoginPage import LoginPage
from testCase.test_Base import BaseTest
from Utility.customLogger import LogGen
import time
import allure

class Test_006_Login(BaseTest):
    logger = LogGen.loggen()


    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_page_title(self,setup):
        self.driver = setup
        self.logger.info("*************** Test_006 Verifying Login Page Test *****************")
        self.logger.info("****Started Login page title test ****")
        self.loginPage=LoginPage(self.driver)
        self.logger.info("****Opening URL****")
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        if title == TestData.LOGIN_PAGE_TITLE:
            self.logger.info("**** Home Login title test passed ****")
            assert True
        else:

            self.driver.save_screenshot(".\\Screenshot\\" + "test_home_page_title.png")
            self.logger.error("**** Home page title test failed****")
            assert False

        self.driver.close()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_login(self,setup):
        self.driver = setup
        self.logger.info("***********TC_007 Verifying Invalid Login Test***********")
        self.logger.info("****Started Login Test****")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(TestData.InvalidUsername)
        self.loginPage.setPassword(TestData.InvalidPassword)
        self.loginPage.clickLogin()
        time.sleep(5)
        act_title=self.driver.title
        print("title->>"+act_title)
        if act_title == TestData.HOME_PAGE_TITLE:
            self.logger.info("****Invalid Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            allure.attach(self.driver.get_screenshot_as_png(), name='testInvalidLogin',
                          attachment_type=AttachmentType.PNG)
            #self.driver.save_screenshot(".\\Screenshot\\" + "test_Invalidlogin.png")
            assert False

        self.driver.close()




