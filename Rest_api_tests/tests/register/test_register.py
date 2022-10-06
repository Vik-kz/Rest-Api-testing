import pytest
import requests
import allure
from api import Register
from model import RegisterUser

URL = "https://stores-tests-api.herokuapp.com"

class TestRegisterUser:
 @allure.feature("test_registration")
 @allure.story("register_user_valid_data")
 @allure.severity("Normal")
 def test_register_user(self):
  with allure.step("Отправляем запрос на регистрацию"):
    body = RegisterUser.random()
    response = Register(url=URL).register_user(body=body)
  with allure.step("Проверяем, что статус код = 201"):
    assert response.status_code == 201, f"response status coide is not 201 {response.status_code}"
  with allure.step("Проверяем сообщение в теле ответа, что юзер добавлен"):
    assert response.json()["message"] == "User created successfully."
  with allure.step("Проверяем, что uuid в ответе не пустой"):
    assert response.json()["uuid"] is not None

 @allure.feature("test_registration")
 @allure.story("register_user_with_empty_field")
 @allure.severity('Normal')
 def test_register_user_with_empty_field(self,register_user):
   with allure.step("Отправляем запрос на регистрацию"):
    response = register_user
   with allure.step("Проверяем,что статус код = 400"):
    assert response.status_code == 400
   with allure.step("Проверяем сообщение в теле ответа сообщение о том, что поля обязательны для заполнения"):
    assert response.json()["message"] == "Username and password are required fields"