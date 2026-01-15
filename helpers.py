import string
import random
import allure
import requests

from endpoints import Endpoints


@allure.step('Отправляем POST запрос - {title}')
def send_post_request(url, data, title):
    response = requests.post(url, data)
    return response

@allure.step('Удаляем пользователя с почтой {email}')
def delete_user(token, email):
    headers = {
        'Authorization': token
    }

    requests.delete(Endpoints.MAIN_PAGE + Endpoints.DELETE_USER, headers=headers)

def generate_random_string():
    length = 10
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_user_email():
    return f'{generate_random_string()}@mail.ru'

def register_new_user():
    payload = {
        'email': generate_user_email(),
        'password':generate_random_string(),
        'name': generate_random_string()
    }
    data = {
        'email': payload['email'],
        'password': payload['password']
    }

    response = send_post_request(Endpoints.MAIN_PAGE + Endpoints.CREATE_USER, payload, 'Создание нового пользователя')

    if response.status_code == 200:
        credentials = response.json()
        data['accessToken'] = credentials.get('accessToken')

    return data

@allure.step('Создаем данные для нового пользователя')
def create_user_data():
    data = {
        'email': generate_user_email(),
        'password': generate_random_string(),
        'name': generate_random_string()
    }

    return data
