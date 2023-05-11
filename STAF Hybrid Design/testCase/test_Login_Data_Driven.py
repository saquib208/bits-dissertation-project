import pytest
from Configuration.config import TestData
from pageObject.LoginPage import LoginPage
from testCase.test_Base import BaseTest
from Utility.customLogger import LogGen
from Utility import XLUtility
import time


class Test_002_Login_DDT(BaseTest):
    logger = LogGen.loggen()
    path = TestData.excel_path

    @pytest.mark.regression
    def test_DDT_login(self,setup):
        self.driver = setup
        self.logger.info("***********TC_002 Verifying Data Driven Login Test***********")
        self.loginPage=LoginPage(self.driver)
        self.logger.info("****Started Login Test****")

        self.rows = XLUtility.getRowCount(self.path, 'Sheet1')
        print(f'Number of rows...{self.rows}')
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtility.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtility.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtility.readData(self.path, 'Sheet1', r, 3)
            time.sleep(5)
            self.logger.info(f"Username-->>{self.user}")
            self.logger.info(f"Password-->>{self.password}")
            self.loginPage.setUserName(self.user)
            self.loginPage.setPassword(self.password)
            self.loginPage.clickLogin()
            time.sleep(10)
            current_url=self.driver.current_url
            if current_url == TestData.home_page_url:
                if self.exp == 'Pass':
                    self.logger.info("****Login test passed ****")
                    self.loginPage.clickLogout()
                    lst_status.append('Pass')
                elif self.exp =='Fail':
                    self.logger.info("****************Fail*********")
                    self.loginPage.clickLogout()
                    lst_status.append("Fail")
                    self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            elif current_url==TestData.login_page_url:
                if self.exp == 'Pass':
                    lst_status.append("Fail")
                    self.logger.error("****Login test failed ****")
                    self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")

                elif self.exp == 'Fail':
                    self.logger.info("**** TC passed ****")
                    lst_status.append("Pass")

        print(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            assert False

        self.driver.close()






