import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocator


class OrderFeedPage(BasePage):
    @allure.step('Ждем загрузки страницы ленты заказов')
    def wait_for_order_feed_page_load(self):
        super().wait_for_load(OrderFeedPageLocator.ORDERS_LIST)

    @allure.step('Кликаем на кнопку "Конструктор" в навигации')
    def click_constructor_button(self):
        super().wait_and_click_on_element(OrderFeedPageLocator.CONSTRUCTOR_BUTTON)

    @allure.step('Получаем количество заказов за все время')
    def get_all_time_orders_count(self):
        return super().wait_and_get_text(OrderFeedPageLocator.ALL_TIME_ORDERS_COUNT)

    @allure.step('Получаем количество заказов за сегодня')
    def get_today_orders_count(self):
        return super().wait_and_get_text(OrderFeedPageLocator.TODAY_ORDERS_COUNT)
    
    @allure.step('Получаем номер заказа')
    def get_cooking_order(self):
        return super().wait_and_get_text(OrderFeedPageLocator.COOKING_ORDER)
