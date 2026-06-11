from selenium.webdriver.common.by import By

class HomePageLocators:
    # Заголовок "Соберите бургер"
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    
    # Заголовок "Лента заказов"
    FEED_HEADER = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    
    # Первый ингредиент в списке 
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    
    # Всплывающее окно
    MODAL_WINDOW = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    
    # Крестик закрытия всплывающего окна
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    
    # Счётчик на первой булке
    INGREDIENT_COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter__num_')])[1]")
    
    # Оверлей всплывающего окна
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    
    # Поле куда складываются ингридиенты
    CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")

    # Синий счётчик на первой булке
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num_')]")

    # Краторная булка N-200i
    BUN_KRATOR = (By.XPATH, "//a[.//img[@alt='Краторная булка N-200i']]")
    BUN_KRATOR_COUNTER = (By.XPATH, "//a[.//img[@alt='Краторная булка N-200i']]//p[contains(@class, 'counter_counter__num_')]")

    #  Флюоресцентная булка R2-D3
    BUN_FLUOR = (By.XPATH, "//a[.//img[@alt='Флюоресцентная булка R2-D3']]")
    BUN_FLUOR_COUNTER = (By.XPATH, "//a[.//img[@alt='Флюоресцентная булка R2-D3']]//p[contains(@class, 'counter_counter__num_')]")

    # Соус Spicy-X
    SAUCE_SPICY = (By.XPATH, "//a[.//img[@alt='Соус Spicy-X']]")
    SAUCE_SPICY_COUNTER = (By.XPATH, "//a[.//img[@alt='Соус Spicy-X']]//p[contains(@class, 'counter_counter__num_')]")

    # Соус фирменный Space Sauce 
    SAUCE_SPACE = (By.XPATH, "//a[.//p[text()='Соус фирменный Space Sauce']]")
    SAUCE_SPACE_COUNTER = (By.XPATH, "//a[.//p[text()='Соус фирменный Space Sauce']]//p[contains(@class, 'counter_counter__num')]")

    # Соус традиционный Галактический
    SAUCE_GALAXY = (By.XPATH, "//a[.//p[text()='Соус традиционный галактический']]")
    SAUCE_GALAXY_COUNTER = (By.XPATH, "//a[.//p[text()='Соус традиционный галактический']]//p[contains(@class, 'counter_counter__num')]")


    #  Соус с шипами Антарианского плоскоходца
    SAUCE_ANTARIAN = (By.XPATH, "//a[.//p[contains(text(), 'Соус с шипами Антарианского плоскоходца')]]")
    SAUCE_ANTARIAN_COUNTER = (By.XPATH, "//a[.//p[contains(text(), 'Соус с шипами Антарианского плоскоходца')]]//p[contains(@class, 'counter_counter__num_')]")

    #  Мясо бессмертных моллюсков Protostomia
    FILLING_MOLUSK = (By.XPATH, "//a[.//p[contains(text(), 'Мясо бессмертных моллюсков Protostomia')]]")
    FILLING_MOLUSK_COUNTER = (By.XPATH, "//a[.//p[contains(text(), 'Мясо бессмертных моллюсков Protostomia')]]//p[contains(@class, 'counter_counter__num_')]")

    # Говяжий метеорит (отбивная)
    FILLING_METEORITE = (By.XPATH, "//a[.//img[@alt='Говяжий метеорит (отбивная)']]")
    FILLING_METEORITE_COUNTER = (By.XPATH, "//a[.//img[@alt='Говяжий метеорит (отбивная)']]//p[contains(@class, 'counter_counter__num_')]")

    # Биокотлета из марсианской Магнолии
    FILLING_BIO_CUTLET = (By.XPATH, "//a[.//img[@alt='Биокотлета из марсианской Магнолии']]")
    FILLING_BIO_CUTLET_COUNTER = (By.XPATH, "//a[.//img[@alt='Биокотлета из марсианской Магнолии']]//p[contains(@class, 'counter_counter__num_')]")

    # Филе Люминесцентного тетраодонтимформа
    FILLING_FISH = (By.XPATH, "//a[.//img[@alt='Филе Люминесцентного тетраодонтимформа']]")
    FILLING_FISH_COUNTER = (By.XPATH, "//a[.//img[@alt='Филе Люминесцентного тетраодонтимформа']]//p[contains(@class, 'counter_counter__num_')]")

    # Хрустящие минеральные кольца
    FILLING_RINGS = (By.XPATH, "//a[.//img[@alt='Хрустящие минеральные кольца']]")
    FILLING_RINGS_COUNTER = (By.XPATH, "//a[.//img[@alt='Хрустящие минеральные кольца']]//p[contains(@class, 'counter_counter__num_')]")

    # Плоды Фалленианского дерева
    FILLING_FRUITS = (By.XPATH, "//a[.//img[@alt='Плоды Фалленианского дерева']]")
    FILLING_FRUITS_COUNTER = (By.XPATH, "//a[.//img[@alt='Плоды Фалленианского дерева']]//p[contains(@class, 'counter_counter__num_')]")

    # Кристаллы марсианских альфа-сахаридов
    FILLING_CRYSTALS = (By.XPATH, "//a[.//img[@alt='Кристаллы марсианских альфа-сахаридов']]")
    FILLING_CRYSTALS_COUNTER = (By.XPATH, "//a[.//img[@alt='Кристаллы марсианских альфа-сахаридов']]//p[contains(@class, 'counter_counter__num_')]")

    # Мини-салат Экзо-Плантаго
    FILLING_SALAD = (By.XPATH, "//a[.//img[@alt='Мини-салат Экзо-Плантаго']]")
    FILLING_SALAD_COUNTER = (By.XPATH, "//a[.//img[@alt='Мини-салат Экзо-Плантаго']]//p[contains(@class, 'counter_counter__num_')]")

    # Сыр с астероидной плесенью
    FILLING_CHEESE = (By.XPATH, "//a[.//img[@alt='Сыр с астероидной плесенью']]")
    FILLING_CHEESE_COUNTER = (By.XPATH, "//a[.//img[@alt='Сыр с астероидной плесенью']]//p[contains(@class, 'counter_counter__num_')]")

    # Вкладки меню конструктора (Булки, Соусы, Начинки)
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
