from selenium.webdriver.common.by import By

class LoginPageLocator:
    EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Войти"]')
