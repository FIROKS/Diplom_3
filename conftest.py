import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from endpoints import Endpoints
from helpers import delete_user, register_new_user


@pytest.fixture(scope='session', params=['Chrome', 'Firefox'])
def driver(request):
    driver = None

    if (request.param == 'Chrome'):
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def delete_user_after_test(driver):
    user_data = register_new_user()

    yield {
        'driver': driver,
        'user_data': user_data
    }

    try:
        delete_user(user_data['accessToken'], user_data['email'])
        print(f'Удален пользователь с email: {user_data['email']}')
    except Exception as e:
        print(f'Ошибка удаления пользователя с email: {user_data['email']}: {e}')

@pytest.fixture(scope="function")
def login(delete_user_after_test):
    user_data = delete_user_after_test['user_data']
    login_page = LoginPage(delete_user_after_test['driver'])
    login_page.go_to_page(Endpoints.MAIN_PAGE + Endpoints.LOGIN_PAGE)

    login_page.fill_email_input(user_data['email'])
    login_page.fill_password_input(user_data['password'])
    login_page.click_confirm_button()

    return delete_user_after_test['driver']
