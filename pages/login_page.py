from stepik_auto_tests_project.pages.base_page import BasePage
from stepik_auto_tests_project.pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"
        # реализуйте проверку на корректный url адрес
        #assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # реализуйте проверку, что есть форма логина
        #assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REG), "Login registration is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        #assert True
