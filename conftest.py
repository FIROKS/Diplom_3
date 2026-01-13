import pytest
from selenium import webdriver


@pytest.fixture(scope='session', params=['Chrome', 'Firefox'])
def driver(request):
    driver = None

    if (request.param == 'Chrome'):
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver

    driver.quit()
