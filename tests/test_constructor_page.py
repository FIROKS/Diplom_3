import allure

from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from endpoints import Endpoints


class TestConstructorPage:
    @allure.title('Переход по клику на кнопку «Конструктор»')
    def test_go_to_constructor_using_nav_button(self, driver):
        order_feed_page = OrderFeedPage(driver)
        constructor_page = ConstructorPage(driver)
        order_feed_page.go_to_page(Endpoints.MAIN_PAGE + Endpoints.ORDER_FEED_PAGE)

        order_feed_page.click_constructor_button()
        constructor_page.wait_for_constructor_page_load()
        
        assert constructor_page.get_current_url() == Endpoints.MAIN_PAGE

    @allure.title('Переход по клику на кнопку «Лента заказов»')
    def test_go_to_order_feed_using_nav_button(self, driver):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        constructor_page.go_to_page(Endpoints.MAIN_PAGE)

        constructor_page.click_order_feed_button()
        order_feed_page.wait_for_order_feed_page_load()

        assert order_feed_page.get_current_url() == Endpoints.MAIN_PAGE + Endpoints.ORDER_FEED_PAGE

    @allure.title('Клик на ингредиент, вызывает всплывающее окно с деталями')
    def test_show_ingredient_details_popup(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_page(Endpoints.MAIN_PAGE)

        constructor_page.click_on_ingredient_element()
        modal_class = constructor_page.get_ingredient_modal_class()

        assert '_opened' in modal_class

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_page(Endpoints.MAIN_PAGE)

        constructor_page.click_on_ingredient_element()
        constructor_page.click_modal_close_button()
        modal_class = constructor_page.get_ingredient_modal_class()

        assert '_opened' not in modal_class

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_increasing_amount_of_added_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_page(Endpoints.MAIN_PAGE)
        initial_amount = constructor_page.get_ingredient_amount()

        constructor_page.add_ingredient()       
        result_amount = constructor_page.get_ingredient_amount()

        assert initial_amount < result_amount
