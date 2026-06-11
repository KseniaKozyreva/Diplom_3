from selenium.webdriver.common.by import By

class OrderFeedLocators:
    # Заголовок страницы
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    # "Выполнено за все время"
    COUNTER_ALL_TIME = (By.XPATH, "//*[contains(text(), 'Выполнено за все время')]/following-sibling::p")

    # "Выполнено за сегодня" 
    COUNTER_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    # Список номеров заказов в блоке "В работе"
    ORDERS_IN_WORK_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")

    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Номер готового заказа внутри всплывающего окна
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_') or contains(@class, 'OrderDetails_id_')]")

    # Крестик для закрытия всплывающего окна с номером заказа
    CLOSE_ORDER_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_')]")
