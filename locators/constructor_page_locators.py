from selenium.webdriver.common.by import By

class ConstructorPageLocator:
    INGREDIENTS_CONTAINER = (By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer")]')
    ORDER_FEED_BUTTON = (By.XPATH, '//nav[contains(@class, "AppHeader_header__nav")]//a[@href="/feed"]')
    INGREDIENT_ELEMENT = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]')
    INGREDIENT_MODAL_OPENED = (By.XPATH, '//section[contains(@class, "Modal_modal")]')
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "Modal_modal__close")]')
    BURGER_CONSTRUCTOR = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    INGREDIENT_COUNT = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]//p[contains(@class, "counter_counter__num")]')
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')    
    SUCCESS_MODAL = (
        By.XPATH,
        '//section[contains(@class, "Modal_modal_opened")]/following::div[starts-with(@class, "Modal_modal__")]')
