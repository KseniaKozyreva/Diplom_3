import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.common.exceptions import TimeoutException

class OrderFeedPage(BasePage):

    @allure.step("Дождаться загрузки страницы Ленты заказов")
    def wait_for_feed_to_load(self):
        self.wait_for_element_visible(OrderFeedLocators.FEED_TITLE)

    @allure.step("Получить значение счетчика 'Выполнено за все время'")
    def get_counter_all_time(self):
        return self.get_element_text_as_int(OrderFeedLocators.COUNTER_ALL_TIME)

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_counter_today(self):
        return self.get_element_text_as_int(OrderFeedLocators.COUNTER_TODAY)

    @allure.step("Проскроллить Ленту заказов в самый низ")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Проверить наличие номера {order_number} в разделе 'В работе'")
    def is_order_in_work(self, order_number):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        clean_number = str(order_number).lstrip('0').replace('#', '')
        
        try:
            order_locator = (By.XPATH, f"//*[contains(text(), '{clean_number}')]")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(order_locator))
            return True
        except:
            return False
