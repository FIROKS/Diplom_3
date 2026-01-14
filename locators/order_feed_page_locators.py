from selenium.webdriver.common.by import By


class OrderFeedPageLocator:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//nav[contains(@class, "AppHeader_header__nav")]//a[@href="/"]')
    ORDERS_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')
    ALL_TIME_ORDERS_COUNT = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY_ORDERS_COUNT = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    COOKING_ORDERS_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]')
    COOKING_ORDER = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
