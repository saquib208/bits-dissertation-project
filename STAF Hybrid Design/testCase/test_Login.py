import pytest
from allure_commons.types import AttachmentType

from Configuration.config import TestData
from pageObject.LoginPage import LoginPage

from Utility.customLogger import LogGen
import time
import allure

class Test_001_Login():
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self,setup):
        self.logger.info("*************** Test_001 Verifying Home Page Test *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.loginPage=LoginPage(self.driver)
        self.logger.info("****Opening URL****")
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        if title == TestData.LOGIN_PAGE_TITLE:
            self.logger.info("**** Home page title test passed ****")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_home_page_title.png")
            allure.attach(self.driver.get_screenshot_as_png(), name='testInvalidLogin',
                          attachment_type=AttachmentType.PNG)
            self.logger.error("**** Home page title test failed****")
            assert False

        self.driver.close()


    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***********TC_002 Verifying Login Test***********")
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(TestData.USER_NAME)
        self.loginPage.setPassword(TestData.PASSWORD)
        self.loginPage.clickLogin()
        time.sleep(5)
        act_title=self.driver.title
        print("title->>"+act_title)
        if act_title == TestData.HOME_PAGE_TITLE:
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            #self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            allure.attach(self.driver.get_screenshot_as_png(), name='testInvalidLogin',
                          attachment_type=AttachmentType.PNG)
            assert False

        self.driver.close()




