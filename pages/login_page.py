import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    @allure.step("Авторизоваться пользователем")
    def login_user(self, email, password):
        self.wait_for_element_visible(LoginLocators.LOGIN_EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*LoginLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
        
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON_ON_PAGE))
        self.click_via_js(LoginLocators.LOGIN_BUTTON_ON_PAGE)
