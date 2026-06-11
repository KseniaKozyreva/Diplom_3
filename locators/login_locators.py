from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    LOGIN_PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON_ON_PAGE = (By.XPATH, "//form[contains(@class, 'Auth_form')]//button")
