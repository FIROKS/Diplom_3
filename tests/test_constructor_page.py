import allure

from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from locators.constructor_page_locators import ConstructorPageLocator
from locators.order_feed_page_locators import OrderFeedPageLocator
from endpoints import Endpoints


class TestConstructorPage:
    @allure.title('Переход по клику на кнопку «Конструктор»')
    def test_go_to_constructor_using_nav_button(self, driver):
        orderFeedPage = OrderFeedPage(driver)
        constructorPage = ConstructorPage(driver)
        orderFeedPage.go_to_page(Endpoints.MAIN_PAGE + Endpoints.ORDER_FEED_PAGE)

        orderFeedPage.click_constructor_button()
        constructorPage.wait_for_constructor_page_load()
        
        assert constructorPage.get_current_url() == Endpoints.MAIN_PAGE

    @allure.title('Переход по клику на кнопку «Лента заказов»')
    def test_go_to_order_feed_using_nav_button(self, driver):
        constructorPage = ConstructorPage(driver)
        orderFeedPage = OrderFeedPage(driver)
        constructorPage.go_to_page(Endpoints.MAIN_PAGE)

        constructorPage.click_order_feed_button()
        orderFeedPage.wait_for_order_feed_page_load()

        assert orderFeedPage.get_current_url() == Endpoints.MAIN_PAGE + Endpoints.ORDER_FEED_PAGE

    @allure.title('Клик на ингредиент, вызывает всплывающее окно с деталями')
    def test_show_ingredient_details_popup(self, driver):
        constructorPage = ConstructorPage(driver)
        constructorPage.go_to_page(Endpoints.MAIN_PAGE)

        constructorPage.click_on_ingredient_element()
        modal_class = constructorPage.get_ingredient_modal_class()

        assert '_opened' in modal_class

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        constructorPage = ConstructorPage(driver)
        constructorPage.go_to_page(Endpoints.MAIN_PAGE)

        constructorPage.click_on_ingredient_element()
        constructorPage.click_modal_close_button()
        modal_class = constructorPage.get_ingredient_modal_class()

        assert '_opened' not in modal_class

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_increasing_amount_of_added_ingredient(self, driver):
        constructorPage = ConstructorPage(driver)
        constructorPage.go_to_page(Endpoints.MAIN_PAGE)
        initial_amount = constructorPage.get_ingredient_amount()

        constructorPage.add_ingredient()       
        result_amount = constructorPage.get_ingredient_amount()

        assert initial_amount < result_amount
