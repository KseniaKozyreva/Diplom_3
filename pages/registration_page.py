import allure
from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators

class RegistrationPage(BasePage):
    @allure.step("Зарегистрировать пользователя")
    def register_user(self, name, email, password):
        self.wait_for_element_visible(RegistrationLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*RegistrationLocators.EMAIL_INPUT_REG).send_keys(email)
        self.driver.find_element(*RegistrationLocators.PASSWORD_INPUT_REG).send_keys(password)
        self.click_via_js(RegistrationLocators.REG_BUTTON)
