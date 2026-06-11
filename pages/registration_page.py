import allure
from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators

class RegistrationPage(BasePage):
    
    @allure.step("Зарегистрировать пользователя")
    def register_user(self, name, email, password):
        self.fill_field(RegistrationLocators.NAME_INPUT, name)
        
        self.fill_field(RegistrationLocators.EMAIL_INPUT_REG, email)
        
        self.fill_field(RegistrationLocators.PASSWORD_INPUT_REG, password)
        
        self.click_via_js(RegistrationLocators.REG_BUTTON)
