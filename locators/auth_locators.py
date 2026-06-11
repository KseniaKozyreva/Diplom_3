from selenium.webdriver.common.by import By

class RegistrationLocators:
    # Поле имя 
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    # Поле email
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка регистрации 
    REG_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
   