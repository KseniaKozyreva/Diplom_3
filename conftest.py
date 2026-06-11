import pytest
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from generators import generate_email, DEFAULT_PASSWORD
from data import TestData
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        service = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        
        try:
            service = FirefoxService(GeckoDriverManager().install())
            web_driver = webdriver.Firefox(service=service, options=options)
        except Exception:
            web_driver = webdriver.Firefox(options=options)

    web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL)
    
    yield web_driver
    web_driver.quit()


@pytest.fixture
def login_user(driver):
    user_email = generate_email()
    user_password = DEFAULT_PASSWORD
    user_name = "Vasia Pisiaev"
    
    # Инициализируем объекты страниц
    reg_page = RegistrationPage(driver)
    login_page = LoginPage(driver)

    # 1. Шаг регистрации
    driver.get(f"{TestData.BASE_URL}register")
    reg_page.register_user(user_name, user_email, user_password)
    
    # Ожидаем перехода на страницу логина
    WebDriverWait(driver, 15).until(EC.url_contains("/login"))
    
    # 2. Шаг логина
    login_page.login_user(user_email, user_password)

    WebDriverWait(driver, 15).until(EC.url_to_be(TestData.BASE_URL))
    
    yield driver
    
    try:
        token = driver.execute_script("return window.localStorage.getItem('accessToken');")
        if token:
            headers = {"Authorization": token}
            requests.delete(f"{TestData.BASE_URL}api/auth/user", headers=headers)
            print(f"\n[Чистка] Пользователь {user_email} успешно удален из базы данных!")
    except Exception as e:
        print(f"\n[Ошибка чистки] Не удалось удалить пользователя: {e}")
