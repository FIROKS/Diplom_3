import allure

from seletools.actions import drag_and_drop

from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from locators.constructor_page_locators import ConstructorPageLocator
from locators.order_feed_page_locators import OrderFeedPageLocator
from endpoints import Endpoints


class TestConstructorPage:
    @allure.title('Переход по клику на кнопку «Конструктор»')
    def test_go_to_constructor_using_nav_button(self, driver):
        orderFeedPage = OrderFeedPage(driver)
        orderFeedPage.go_to_page(Endpoints.MAIN_PAGE + Endpoints.ORDER_FEED_PAGE)

        orderFeedPage.click_on_constructor_button()
        orderFeedPage.wait_for_load(ConstructorPageLocator.INGREDIENTS_CONTAINER)
        
        assert orderFeedPage.get_current_url() == Endpoints.MAIN_PAGE

    @allure.title('Переход по клику на кнопку «Лента заказов»')
    def test_go_to_order_feed_using_nav_button(self, driver):
        constructorPage = ConstructorPage(driver)
        constructorPage.go_to_page(Endpoints.MAIN_PAGE)

        constructorPage.wait_and_click_on_element(ConstructorPageLocator.ORDER_FEED_BUTTON)
        constructorPage.wait_for_load(OrderFeedPageLocator.ORDERS_LIST)

        assert constructorPage.get_current_url() == Endpoints.MAIN_PAGE + Endpoints.ORDER_FEED_PAGE

    @allure.title('Клик на ингредиент, вызывает всплывающее окно с деталями')
    def test_show_ingredient_details_popup(self, driver):
        constructorPage = ConstructorPage(driver)
        constructorPage.go_to_page(Endpoints.MAIN_PAGE)

        constructorPage.wait_and_click_on_element(ConstructorPageLocator.INGREDIENT_ELEMENT)
        modal_class = constructorPage.wait_and_find_element(ConstructorPageLocator.INGREDIENT_MODAL).get_attribute('class')

        assert '_opened' in modal_class

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        constructorPage = ConstructorPage(driver)
        constructorPage.go_to_page(Endpoints.MAIN_PAGE)

        constructorPage.wait_and_click_on_element(ConstructorPageLocator.INGREDIENT_ELEMENT)
        constructorPage.wait_and_click_on_element(ConstructorPageLocator.INGREDIENT_MODAL_CLOSE_BUTTON)
        modal_class = constructorPage.wait_and_find_element(ConstructorPageLocator.INGREDIENT_MODAL).get_attribute('class')

        assert '_opened' not in modal_class

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_increasing_amount_of_added_ingredient(self, driver):
        constructorPage = ConstructorPage(driver)
        constructorPage.go_to_page(Endpoints.MAIN_PAGE)
        source = constructorPage.wait_and_find_element(ConstructorPageLocator.INGREDIENT_ELEMENT)
        target = constructorPage.wait_and_find_element(ConstructorPageLocator.BURGER_CONSTRUCTOR)
        initial_amount = constructorPage.wait_and_get_text(ConstructorPageLocator.INGREDIENT_COUNT)

        drag_and_drop(driver, source, target)
        result_amount = constructorPage.wait_and_get_text(ConstructorPageLocator.INGREDIENT_COUNT)

        assert initial_amount < result_amount
