import pytest
import requests
import allure
from api import Register
from model import RegisterUser


class TestAuthUser:
 @allure.feature("test_authorization")
 @allure.story("user_auth")
 @allure.severity('Critical')
 def test_user_auth(self):
   with allure.step("Отправляем запрос на добавление юзера"):
    response = Register.register_app_user
    return response
   with allure.step("Отправляем запрос на авторизацию"):
    response = Register.auth_app_user
   with allure.step("Проверяем , что статус код = 200"):
    assert response.status_code == 200, f" response status code is not 200 {response.status_code}"
   with allure.step("Проверяем что токен авторизации не пустой"):
    assert response.json()["access_token"] is not None

 @allure.feature("test_authorization")
 @allure.story("user_auth_invalid_data")
 @allure.severity('Normal')
 def test_user_auth_invalid_data(self, auth_user_invalid_data):
   with allure.step("Отправляем запрос на аторизацию с неправильными данными"):
    response = auth_user_invalid_data
   with allure.step("Проверяем что указанные данные не верны и статус код = 401"):
    assert response.status_code == 401, f"response status code is not 401 {response.status_code}"