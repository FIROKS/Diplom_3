import allure

from seletools.actions import drag_and_drop

from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocator
from data import Config


class ConstructorPage(BasePage):
    @allure.step('Ждем загрузки страницы конструктора')
    def wait_for_constructor_page_load(self):
        super().wait_for_load(ConstructorPageLocator.INGREDIENTS_CONTAINER)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_order_feed_button(self):
        super().wait_and_click_on_element(ConstructorPageLocator.ORDER_FEED_BUTTON)

    @allure.step('Нажимаем на ингредиент')
    def click_on_ingredient_element(self):
        super().wait_and_click_on_element(ConstructorPageLocator.INGREDIENT_ELEMENT)
        
    def get_ingredient_modal_class(self):
        return super().wait_and_find_element(ConstructorPageLocator.INGREDIENT_MODAL_OPENED).get_attribute('class')
    
    @allure.step('Нажимаем на кнопку закрытия модального окна')
    def click_modal_close_button(self):
        super().click_to_element_by_script(ConstructorPageLocator.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step('Нажимаем на кнопку закрытия модального окна')
    def get_ingredient_amount(self):
        return super().wait_and_get_text(ConstructorPageLocator.INGREDIENT_COUNT)
    
    @allure.step('Переносим ингредиент в корзину')
    def add_ingredient(self):
        source = super().wait_and_find_element(ConstructorPageLocator.INGREDIENT_ELEMENT)
        target = super().wait_and_find_element(ConstructorPageLocator.BURGER_CONSTRUCTOR)

        drag_and_drop(self.driver, source, target)
    
    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_order_button(self):
        super().wait_and_click_on_element(ConstructorPageLocator.ORDER_BUTTON)

    @allure.step('Нажимаем на кнопку закрытия окна с идентификатором заказа')
    def click_success_order_close_button(self):
        try:
            super().wait_for_load(ConstructorPageLocator.SUCCESS_MODAL, Config.LONG_WAIT)
            super().wait_and_click_on_element(ConstructorPageLocator.INGREDIENT_MODAL_CLOSE_BUTTON)
        except:
            super().click_to_element_by_script(ConstructorPageLocator.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step('Нажимаем на кнопку "Лента заказов" с помощью скрипта')
    def click_order_feed_button_script(self):
        super().click_to_element_by_script(ConstructorPageLocator.ORDER_FEED_BUTTON)
