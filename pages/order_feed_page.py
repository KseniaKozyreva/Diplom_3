import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

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
        self.execute_js("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Проверить наличие номера {order_number} в разделе 'В работе'")
    def is_order_in_work(self, order_number):
        clean_number = str(order_number).lstrip('0').replace('#', '')
        
        xpath_selector = OrderFeedLocators.ORDER_BY_NUMBER_TEMPLATE.format(number=clean_number)
        
        dynamic_locator = ("xpath", xpath_selector)
        
        return self.is_element_visible(dynamic_locator, timeout=10)
