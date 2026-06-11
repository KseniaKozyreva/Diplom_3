from selenium.webdriver.common.by import By

class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    EMAIL_INPUT_REG = (By.XPATH, "(//input[@name='name'])[2]")
    PASSWORD_INPUT_REG = (By.XPATH, "//input[@name='Пароль']")
    REG_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
