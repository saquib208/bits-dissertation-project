import pytest
from allure_commons.types import AttachmentType
from Utility.video_capture import Record
from Configuration.config import TestData
from pageObject.LoginPage import LoginPage
import cv2
import numpy as np
import pyautogui

from Utility.customLogger import LogGen
import time
import allure

class Test_001_Login():
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        while True:

            resolution = (1920, 1080)
            codec = cv2.VideoWriter_fourcc(*"XVID")
            filename = "Recording.avi"
            fps = 60.0
            out = cv2.VideoWriter(filename, codec, fps, resolution)
            cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Live", 480, 270)
            while True:
                img = pyautogui.screenshot()
                # Convert the screenshot to a numpy array
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                cv2.imshow('Live', frame)
                #key1 = cv2.waitKey(0)
                # if key1 == ord('q'):
                #     break
                self.logger.info("*************** Test_001 Verifying Home Page Test *****************")
                self.logger.info("****Started Home page title test ****")
                self.driver = setup
                self.loginPage = LoginPage(self.driver)
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
                frame=Record.get_frame(self)
                if frame is False:
                    break

            out.release()
            cv2.destroyAllWindows()














