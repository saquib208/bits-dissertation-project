from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

"""" This class is the parent of all pages , contains generic method and utilities """

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_elemnt(self,by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def find_element(self,by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))

    def select_first_value_from_drop_down_list(self,by_locator):
        self.wait_for_elemnt(by_locator)
        a = ActionChains(self.driver)
        m = self.find_element(by_locator)
        a.move_to_element(m).perform()
        a.send_keys(Keys.ARROW_DOWN,Keys.RETURN).perform()
        a.click().perform()

    def select_second_value_from_drop_down_list(self,by_locator):
        self.wait_for_elemnt(by_locator)
        a = ActionChains(self.driver)
        m = self.find_element(by_locator)
        a.move_to_element(m).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN,Keys.RETURN).click().perform()

    def find_elements(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        ele = self.driver.find_elements(*by_locator)
        return ele

    def do_clear(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        element = WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_screenshot(self,path):
        self.driver.save_screenshot(".\\Screenshot\\" + path)