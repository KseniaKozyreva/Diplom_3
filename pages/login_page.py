import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    
    @allure.step("Авторизоваться пользователем")
    def login_user(self, email, password):
        self.fill_field(LoginLocators.LOGIN_EMAIL_INPUT, email)
        
        self.fill_field(LoginLocators.LOGIN_PASSWORD_INPUT, password)
        
        self.click_element(LoginLocators.LOGIN_BUTTON_ON_PAGE)
