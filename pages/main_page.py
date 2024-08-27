from stepik_auto_tests_project.pages.base_page import BasePage
from stepik_auto_tests_project.pages.locators import MainPageLocators
from stepik_auto_tests_project.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
