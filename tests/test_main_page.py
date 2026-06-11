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

    @allure.title("Счётчики ингредиентов: Булки")
    @pytest.mark.parametrize("ing_locator, count_locator", [
        (HomePageLocators.BUN_FLUOR, HomePageLocators.BUN_FLUOR_COUNTER),
        (HomePageLocators.BUN_KRATOR, HomePageLocators.BUN_KRATOR_COUNTER)
    ])
    def test_buns_counters(self, driver, ing_locator, count_locator):
        home = HomePage(driver)
        home.refresh_page()
        home.wait_for_overlay_to_disappear()
        
        initial_count = home.get_counter_value(count_locator)
        home.drag_ingredient_to_basket(ing_locator)
        new_count = home.get_counter_value(count_locator)
        
        assert new_count > initial_count, f"Счетчик для локатора {count_locator} не увеличился!"

    @allure.title("Счётчики ингредиентов: Соусы")
    @pytest.mark.parametrize("ing_locator, count_locator", [
        (HomePageLocators.SAUCE_SPICY, HomePageLocators.SAUCE_SPICY_COUNTER),
        (HomePageLocators.SAUCE_SPACE, HomePageLocators.SAUCE_SPACE_COUNTER),
        (HomePageLocators.SAUCE_GALAXY, HomePageLocators.SAUCE_GALAXY_COUNTER),
        (HomePageLocators.SAUCE_ANTARIAN, HomePageLocators.SAUCE_ANTARIAN_COUNTER)
    ])
    def test_sauces_counters(self, driver, ing_locator, count_locator):
        home = HomePage(driver)
        home.refresh_page()
        home.wait_for_overlay_to_disappear()      
        home.click_sauces_tab()
            
        initial_count = home.get_counter_value(count_locator)
        home.drag_ingredient_to_basket(ing_locator)
        new_count = home.get_counter_value(count_locator)
        
        assert new_count > initial_count, f"Счетчик для локатора {count_locator} не увеличился!"

    @allure.title("Счётчики ингредиентов: Начинки")
    @pytest.mark.parametrize("ing_locator, count_locator", [
        (HomePageLocators.FILLING_MOLUSK, HomePageLocators.FILLING_MOLUSK_COUNTER),
        (HomePageLocators.FILLING_METEORITE, HomePageLocators.FILLING_METEORITE_COUNTER),
        (HomePageLocators.FILLING_BIO_CUTLET, HomePageLocators.FILLING_BIO_CUTLET_COUNTER),
        (HomePageLocators.FILLING_FISH, HomePageLocators.FILLING_FISH_COUNTER),
        (HomePageLocators.FILLING_RINGS, HomePageLocators.FILLING_RINGS_COUNTER),
        (HomePageLocators.FILLING_FRUITS, HomePageLocators.FILLING_FRUITS_COUNTER),
        (HomePageLocators.FILLING_CRYSTALS, HomePageLocators.FILLING_CRYSTALS_COUNTER),
        (HomePageLocators.FILLING_SALAD, HomePageLocators.FILLING_SALAD_COUNTER),
        (HomePageLocators.FILLING_CHEESE, HomePageLocators.FILLING_CHEESE_COUNTER)
    ])
    def test_fillings_counters(self, driver, ing_locator, count_locator):
        home = HomePage(driver)
        home.refresh_page()
        home.wait_for_overlay_to_disappear()
        
        home.click_fillings_tab()
            
        initial_count = home.get_counter_value(count_locator)
        home.drag_ingredient_to_basket(ing_locator)
        new_count = home.get_counter_value(count_locator)
        
        assert new_count > initial_count, f"Счетчик для локатора {count_locator} не увеличился!"
