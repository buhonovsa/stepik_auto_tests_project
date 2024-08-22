from stepik_auto_tests_project.pages.base_page import BasePage
from stepik_auto_tests_project.pages.locators import MainPageLocators
from stepik_auto_tests_project.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        time.sleep(15)
        #alert = self.browser.switch_to.alert
        #alert.accept()
        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

