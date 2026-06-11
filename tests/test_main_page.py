import pytest
import allure
from pages.header_page import HeaderPage
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators


class TestMainPage:

    @allure.title("Переход по клику на кнопку 'Конструктор'")
    def test_click_constructor_opens_constructor(self, driver):
        header = HeaderPage(driver)
        home = HomePage(driver)
        header.click_order_feed()
        header.click_constructor()
        assert home.is_constructor_header_displayed()

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_click_order_feed_opens_feed(self, driver):
        header = HeaderPage(driver)
        home = HomePage(driver)
        header.click_order_feed()
        assert home.is_feed_header_displayed()

    @allure.title("Появление всплывающего окна с деталями при клике на ингредиент")
    def test_click_ingredient_opens_modal(self, driver):
        home = HomePage(driver)
        home.click_ingredient()
        assert home.is_modal_window_displayed()

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_click_close_button_closes_modal(self, driver):
        home = HomePage(driver)
        home.click_ingredient()
        home.click_close_modal()
        
        assert home.is_modal_window_invisible() is True, "Модальное окно деталей ингредиента не закрылось!"

    @allure.title("Счетчики для каждого ингредиента меню")
    @pytest.mark.parametrize("ing_locator, count_locator, tab_method", [
        (HomePageLocators.BUN_FLUOR, HomePageLocators.BUN_FLUOR_COUNTER, None),
        (HomePageLocators.BUN_KRATOR, HomePageLocators.BUN_KRATOR_COUNTER, None),
        
        (HomePageLocators.SAUCE_SPICY, HomePageLocators.SAUCE_SPICY_COUNTER, HomePage.click_sauces_tab),
        (HomePageLocators.SAUCE_SPACE, HomePageLocators.SAUCE_SPACE_COUNTER, HomePage.click_sauces_tab),
        (HomePageLocators.SAUCE_GALAXY, HomePageLocators.SAUCE_GALAXY_COUNTER, HomePage.click_sauces_tab),
        (HomePageLocators.SAUCE_ANTARIAN, HomePageLocators.SAUCE_ANTARIAN_COUNTER, HomePage.click_sauces_tab),
        
        # И здесь тоже пишем просто HomePage:
        (HomePageLocators.FILLING_MOLUSK, HomePageLocators.FILLING_MOLUSK_COUNTER, HomePage.click_fillings_tab),
        (HomePageLocators.FILLING_METEORITE, HomePageLocators.FILLING_METEORITE_COUNTER, HomePage.click_fillings_tab),
        (HomePageLocators.FILLING_BIO_CUTLET, HomePageLocators.FILLING_BIO_CUTLET_COUNTER, HomePage.click_fillings_tab),
        (HomePageLocators.FILLING_FISH, HomePageLocators.FILLING_FISH_COUNTER, HomePage.click_fillings_tab),
        (HomePageLocators.FILLING_RINGS, HomePageLocators.FILLING_RINGS_COUNTER, HomePage.click_fillings_tab),
        (HomePageLocators.FILLING_FRUITS, HomePageLocators.FILLING_FRUITS_COUNTER, HomePage.click_fillings_tab),
        (HomePageLocators.FILLING_CRYSTALS, HomePageLocators.FILLING_CRYSTALS_COUNTER, HomePage.click_fillings_tab),
        (HomePageLocators.FILLING_SALAD, HomePageLocators.FILLING_SALAD_COUNTER, HomePage.click_fillings_tab),
        (HomePageLocators.FILLING_CHEESE, HomePageLocators.FILLING_CHEESE_COUNTER, HomePage.click_fillings_tab)
    ])
    def test_all_ingredients_counters(self, driver, ing_locator, count_locator, tab_method):
        home = HomePage(driver)
        
        home.refresh_page()
        
        home.wait_for_overlay_to_disappear()
        
        if tab_method:
            tab_method(home)
            
        initial_count = home.get_counter_value(count_locator)
        home.drag_ingredient_to_basket(ing_locator)
        new_count = home.get_counter_value(count_locator)
        
        assert new_count > initial_count, f"Счетчик для локатора {count_locator} не увеличился!"
