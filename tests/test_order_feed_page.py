import allure

from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage


class TestOrderFeedPage:
    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_increase_all_time_orders_count(self, login):
        constructor_page = ConstructorPage(login)
        order_feed_page = OrderFeedPage(login)
        constructor_page.click_order_feed_button()
        order_count = order_feed_page.get_all_time_orders_count()
        order_feed_page.click_constructor_button()
        
        constructor_page.add_ingredient()
        constructor_page.click_order_button()
        constructor_page.click_success_order_close_button()
        constructor_page.click_order_feed_button_script()
        new_order_count = order_feed_page.get_all_time_orders_count()

        assert new_order_count > order_count

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_increase_today_orders_count(self, login):
        constructor_page = ConstructorPage(login)
        order_feed_page = OrderFeedPage(login)
        constructor_page.click_order_feed_button()
        order_count = order_feed_page.get_today_orders_count()
        order_feed_page.click_constructor_button()
        
        constructor_page.add_ingredient()
        constructor_page.click_order_button()
        constructor_page.click_success_order_close_button()
        constructor_page.click_order_feed_button_script()
        new_order_count = order_feed_page.get_today_orders_count()

        assert new_order_count > order_count

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_display_order_number(self, login):
        constructor_page = ConstructorPage(login)
        order_feed_page = OrderFeedPage(login)

        constructor_page.add_ingredient()
        constructor_page.click_order_button()
        new_order_id = constructor_page.click_success_order_close_button()
        constructor_page.click_order_feed_button_script()
        cooking_order_id = order_feed_page.get_cooking_order()

        assert new_order_id == cooking_order_id
        