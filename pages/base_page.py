import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Config
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем загрузки страницы')
    def wait_for_load(self, selector):
        WebDriverWait(self.driver, Config.DEFAULT_WAIT).until(expected_conditions.visibility_of_element_located(selector))

    @allure.step('Подождать и нажать на элемент')
    def wait_and_click_on_element(self, selector):
        WebDriverWait(self.driver, Config.DEFAULT_WAIT).until(expected_conditions.visibility_of_element_located(selector))
        self.driver.find_element(*selector).click()

    @allure.step('Скролл до элемента')
    def find_and_focus_by_script(self, selector):
        WebDriverWait(self.driver, Config.DEFAULT_WAIT).until(expected_conditions.presence_of_element_located(selector))
        element_to_focus = self.driver.find_element(*selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_to_focus)
        WebDriverWait(self.driver, Config.DEFAULT_WAIT).until(expected_conditions.element_to_be_clickable(selector))

    @allure.step('Подождать и найти элемент')
    def wait_and_find_element(self, selector):
        WebDriverWait(self.driver, Config.DEFAULT_WAIT).until(expected_conditions.visibility_of_element_located(selector))
        return self.driver.find_element(*selector)
    
    @allure.step('Подождать и получить текст элемента')
    def wait_and_get_text(self, selector):
        WebDriverWait(self.driver, Config.DEFAULT_WAIT).until(expected_conditions.visibility_of_element_located(selector))
        return self.driver.find_element(*selector).text
    
    @allure.step('Подождать и ввести данные')
    def wait_and_fill_input(self, selector, text):
        WebDriverWait(self.driver, Config.DEFAULT_WAIT).until(expected_conditions.visibility_of_element_located(selector))
        self.driver.find_element(*selector).send_keys(text)

    @allure.step('Переходим на страницу - {endpoint}')
    def go_to_page(self, endpoint):
        self.driver.get(endpoint)

    @allure.step('Нажимаем кнопку "Личный кабинет" в шапке')
    def click_profile_button_in_nav(self):
        self.wait_and_click_on_element(BasePageLocators.PROFILE_BUTTON)

    @allure.step('Клик по элементу на странице')
    def click_to_element_by_script(self, selector):
        element = self.wait_and_find_element(selector)
        self.driver.execute_script("arguments[0].click();", element)
        
    def get_current_url(self):
        return self.driver.current_url
    