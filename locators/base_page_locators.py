from selenium.webdriver.common.by import By


class BasePageLocators:
    PROFILE_BUTTON = (By.XPATH, '//nav[contains(@class, "AppHeader_header__nav")]//a[@href="/account"]')
    