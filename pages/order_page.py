import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from locators.order_feed_locators import OrderFeedLocators

class OrderPage(BasePage):

    @allure.step("Перетащить булку в конструктор")
    def add_bun_to_burger(self):
        self.is_element_invisible(HomePageLocators.MODAL_OVERLAY, timeout=30)
        
        self.drag_and_drop_via_js(HomePageLocators.BUN_FLUOR, OrderFeedLocators.CREATE_ORDER_BUTTON)
        
        self.wait_for_element_visible(OrderFeedLocators.CREATE_ORDER_BUTTON, timeout=30)

    @allure.step("Нажать на кнопку 'Оформить заказ'")
    def click_create_order(self):
        self.click_via_js(OrderFeedLocators.CREATE_ORDER_BUTTON)

    @allure.step("Дождаться генерации реального номера заказа и считать его")
    def get_real_order_number(self):
        order_element = self.wait_for_element_visible(OrderFeedLocators.ORDER_NUMBER_IN_MODAL)
        
        self.wait_text_not_present(OrderFeedLocators.ORDER_NUMBER_IN_MODAL, "9999", timeout=30)
        self.wait_text_not_present(OrderFeedLocators.ORDER_NUMBER_IN_MODAL, "0000", timeout=30)
        self.wait_text_not_present(OrderFeedLocators.ORDER_NUMBER_IN_MODAL, "идентификатор заказа", timeout=30)
        
        return order_element.text

    @allure.step("Закрыть модальное окно с номером заказа по крестику")
    def close_order_modal(self):
        self.click_via_js(OrderFeedLocators.CLOSE_ORDER_MODAL_BUTTON)
        self.is_element_invisible(HomePageLocators.MODAL_OVERLAY, timeout=30)

    @allure.step("Нажать на ЛЕНТУ ЗАКАЗА в шапке лендинга")
    def go_to_order_feed(self):
        self.click_via_js(HeaderLocators.ORDER_FEED_BUTTON)
