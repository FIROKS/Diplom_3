import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем загрузки страницы')
    def wait_for_load(self, selector):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(selector))

    @allure.step('Подождать и нажать на элемент')
    def wait_and_click_on_element(self, selector):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(selector))
        self.driver.find_element(*selector).click()

    @allure.step('Подождать и найти элемент')
    def wait_and_find_element(self, selector):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(selector))
        return self.driver.find_element(*selector)
    
    @allure.step('Подождать и получить текст элемента')
    def wait_and_get_text(self, selector):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(selector))
        return self.driver.find_element(*selector).text

    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переходим на страницу - {endpoint}')
    def go_to_page(self, endpoint):
        self.driver.get(endpoint)
    