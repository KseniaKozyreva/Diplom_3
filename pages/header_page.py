import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class HeaderPage(BasePage):

    @allure.step("Клик на кнопку 'Конструктор' в шапке")
    def click_constructor(self):
        self.click_via_js(HeaderLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на кнопку 'Лента заказов' в шапке")
    def click_order_feed(self):
        self.click_via_js(HeaderLocators.ORDER_FEED_BUTTON)
  