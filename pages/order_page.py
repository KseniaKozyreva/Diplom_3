import allure
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from locators.order_feed_locators import OrderFeedLocators

class OrderPage(BasePage):

    @allure.step("Перетащить булку в конструктор")
    def add_bun_to_burger(self):
        # Используем строго expected_conditions для исчезновения оверлея
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(HomePageLocators.MODAL_OVERLAY)
        )
        self.drag_and_drop_via_js(HomePageLocators.BUN_FLUOR, OrderFeedLocators.CREATE_ORDER_BUTTON)
        
        # Используем строго expected_conditions для проверки кликабельности кнопки
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(OrderFeedLocators.CREATE_ORDER_BUTTON)
        )

    @allure.step("Нажать на кнопку 'Оформить заказ'")
    def click_create_order(self):
        self.click_via_js(OrderFeedLocators.CREATE_ORDER_BUTTON)

    @allure.step("Дождаться генерации реального номера заказа и считать его")
    def get_real_order_number(self):
        order_element = self.wait_for_element_visible(OrderFeedLocators.ORDER_NUMBER_IN_MODAL)
        
        WebDriverWait(self.driver, 30).until_not(
            EC.text_to_be_present_in_element(OrderFeedLocators.ORDER_NUMBER_IN_MODAL, "9999")
        )
        WebDriverWait(self.driver, 30).until_not(
            EC.text_to_be_present_in_element(OrderFeedLocators.ORDER_NUMBER_IN_MODAL, "0000")
        )
        WebDriverWait(self.driver, 30).until_not(
            EC.text_to_be_present_in_element(OrderFeedLocators.ORDER_NUMBER_IN_MODAL, "идентификатор заказа")
        )
        
        return order_element.text

    @allure.step("Закрыть модальное окно с номером заказа по крестику")
    def close_order_modal(self):
        self.click_via_js(OrderFeedLocators.CLOSE_ORDER_MODAL_BUTTON)
        
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(HomePageLocators.MODAL_OVERLAY)
        )

    @allure.step("Нажать на ЛЕНТУ ЗАКАЗА в шапке лендинга")
    def go_to_order_feed(self):
        self.click_via_js(HeaderLocators.ORDER_FEED_BUTTON)
