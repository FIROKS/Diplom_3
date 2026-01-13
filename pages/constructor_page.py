import allure

from pages.base_page import BasePage


class ConstructorPage(BasePage):
    @allure.step('Ждем загрузки конструктора')
    def wait_for_load_order_page(self):
        super().wait_for_load(              )
