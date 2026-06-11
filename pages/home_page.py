import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):

    @allure.step("Клик на первый ингредиент")
    def click_ingredient(self):
        self.click_via_js(HomePageLocators.FIRST_INGREDIENT)

    @allure.step("Клик на крестик закрытия окна")
    def click_close_modal(self):
        self.click_via_js(HomePageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Переключить вкладку конструктора на 'Булки'")
    def click_buns_tab(self):
        self.click_via_js(HomePageLocators.BUNS_TAB)

    @allure.step("Переключить вкладку конструктора на 'Соусы'")
    def click_sauces_tab(self):
        self.click_via_js(HomePageLocators.SAUCES_TAB)

    @allure.step("Переключить вкладку конструктора на 'Начинки'")
    def click_fillings_tab(self):
        self.click_via_js(HomePageLocators.FILLINGS_TAB)

    @allure.step("Перетащить ингредиент в корзину конструктора")
    def drag_ingredient_to_basket(self, ingredient_locator):
        self.drag_and_drop_via_js(ingredient_locator, HomePageLocators.CONSTRUCTOR_BASKET)

    @allure.step("Получить значение счётчика ингредиента")
    def get_counter_value(self, counter_locator):
        return self.get_element_text_as_int(counter_locator)

    @allure.step("Проверить, отображается ли заголовок конструктора")
    def is_constructor_header_displayed(self):
        return self.wait_for_element_visible(HomePageLocators.CONSTRUCTOR_HEADER).is_displayed()

    @allure.step("Проверить, отображается ли заголовок ленты заказов")
    def is_feed_header_displayed(self):
        return self.wait_for_element_visible(HomePageLocators.FEED_HEADER).is_displayed()

    @allure.step("Проверить, отображается ли модальное окно")
    def is_modal_window_displayed(self):
        return self.wait_for_element_visible(HomePageLocators.MODAL_WINDOW).is_displayed()

    @allure.step("Проверить, исчезло ли модальное окно деталей ингредиента")
    def is_modal_window_invisible(self):
        return self.is_element_invisible(HomePageLocators.MODAL_WINDOW, timeout=5)

    @allure.step("Дождаться, пока закроется оверлей модального окна")
    def wait_for_overlay_to_disappear(self):
        self.is_element_invisible(HomePageLocators.MODAL_OVERLAY, timeout=3)
