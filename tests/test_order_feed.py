import pytest
import allure
from pages.order_feed_page import OrderFeedPage
from pages.order_page import OrderPage

@allure.suite("Лента заказов")
class TestOrderFeed:

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_counter_all_time_increases(self, login_user):
        feed = OrderFeedPage(login_user)
        order = OrderPage(login_user)
        
        order.add_bun_to_burger()
        order.click_create_order()
        order.get_real_order_number()  
        order.close_order_modal()
        
        order.go_to_order_feed()
        feed.wait_for_feed_to_load()
        
        feed.scroll_to_bottom()
        
        new_all_time = feed.get_counter_all_time()
        assert new_all_time > 0, "Счётчик за всё время пустой!"

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_counter_today_increases(self, login_user):
        feed = OrderFeedPage(login_user)
        order = OrderPage(login_user)
        
        order.add_bun_to_burger()
        order.click_create_order()
        order.get_real_order_number()  
        order.close_order_modal()
        
        order.go_to_order_feed()
        feed.wait_for_feed_to_load()
        
        feed.scroll_to_bottom()
        
        new_today = feed.get_counter_today()
        assert new_today > 0, "Счётчик за сегодня пустой!"

    @allure.title("После оформления заказа его номер появляется на странице Ленты")
    def test_order_number_appears_in_feed(self, login_user):
        feed = OrderFeedPage(login_user)
        order = OrderPage(login_user)
        
        order.add_bun_to_burger()
        order.click_create_order()
        
        real_number = order.get_real_order_number()
        order.close_order_modal()
        
        order.go_to_order_feed()
        feed.wait_for_feed_to_load()
        
        feed.scroll_to_bottom()
        
        is_found = feed.is_order_in_work(real_number)
        assert is_found is True, f"Реальный номер заказа #{real_number} не отобразился на странице Ленты!"
