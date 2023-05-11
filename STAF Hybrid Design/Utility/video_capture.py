from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import cv2
import numpy as np
import pyautogui


class Record():
    def __init__(self, object, file_name="video", flags=cv2.IMREAD_COLOR):
        self.object = object
        self.flags = flags
        #self.size=size
        fps = 60.0
        resolution = (1920, 1080)
        codec = cv2.VideoWriter_fourcc(*"XVID")
        #fourcc = cv2.VideoWriter_fourcc(*'mp4v')


        self.out = cv2.VideoWriter(f"{file_name}.avi", codec, fps, resolution)

    def get_frame(self):
        try:
            if isinstance(self.object, WebDriver):
                im_arr = np.frombuffer(
                    self.object.get_screenshot_as_png(), dtype=np.uint8)
            elif isinstance(self.object, WebElement):
                im_arr = np.frombuffer(
                    self.object.screenshot_as_png, dtype=np.uint8)

            self.frame = cv2.imdecode(im_arr, flags=self.flags)
            return self.frame

        except:
            return False

    # def capture(self):
    #     frame = cv2.resize(self.frame, self.size)
    #     self.out.write(frame)
    #     #cv2.imshow('Live', frame)
    #     return frame

    def capture2(self):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.out.write(frame)
        cv2.imshow('Live', frame)
        return frame

    def save(self):
        self.out.release()



    def screen_capture(self,frame):
        resolution = (1920, 1080)


        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*"XVID")

        # Specify name of Output file
        filename = "Recording.avi"

        # Specify frames rate. We can choose any
        # value and experiment with it
        fps = 60.0

        # Creating a VideoWriter object
        out = cv2.VideoWriter(filename, codec, fps, resolution)

        # Create an Empty window
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

        # Resize this window
        cv2.resizeWindow("Live", 480, 270)

        while True:
            # Take screenshot using PyAutoGUI
            img = pyautogui.screenshot()

            # Convert the screenshot to a numpy array
            frame = np.array(img)

            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write it to the output file
            out.write(frame)


            # Optional: Display the recording screen
            cv2.imshow('Live', frame)


            # Stop recording when we press 'q'
            key1= cv2.waitKey(0)

            # if key1 == ord('q'):
            #     break

            if frame is False:
                break


        # Release the Video writer
        out.release()

        # Destroy all windows
        cv2.destroyAllWindows()

#print(screen_capture())

#
# time.sleep(10)
# print(screen_capture(stop=False))
#
#
#


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
            key1= cv2.waitKey(0)
            # if key1 == ord('q'):
            #     break


            if frame is False:
                break

        out.release()
        cv2.destroyAllWindows()