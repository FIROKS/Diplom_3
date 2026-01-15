import allure

from pages.base_page import BasePage

from locators.login_page_locators import LoginPageLocator


class LoginPage(BasePage):
    def wait_for_login_page_load(self):
        super().wait_for_load(LoginPageLocator.EMAIL_INPUT)

    @allure.step('Заполняем поле "email"')
    def fill_email_input(self, email):
        super().wait_and_fill_input(LoginPageLocator.EMAIL_INPUT, email)

    @allure.step('Заполняем поле "password"')
    def fill_password_input(self, password):
        super().wait_and_fill_input(LoginPageLocator.PASSWORD_INPUT, password)

    @allure.step('Нажимаем кнопку "Войти"')
    def click_confirm_button(self):
        super().wait_and_click_on_element(LoginPageLocator.CONFIRM_BUTTON)
