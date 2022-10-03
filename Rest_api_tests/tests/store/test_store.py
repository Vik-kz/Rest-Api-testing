import pytest
import requests
import allure
from api import Register,UserInformation,AuthApp
from model import RegisterUser,AddUserInfo,Store


URL = "https://stores-tests-api.herokuapp.com/store/"

class TestStore:
 @allure.feature("test_store")
 @allure.story("add_store")
 @allure.severity('Critical')
 def test_add_store(self):
   with allure.step("Отправляем запрос на добавление информации о юзере"):
     response = UserInformation.add_user_information
     return response
   with allure.step("Отправляем запрос на добавление магазина"):
     headers = AuthApp.get_token
     name_store = Store.add_random_store
     response_2 = requests.post(url=URL+f"{name_store}", headers=headers)
     return response_2
   with allure.step("Проверяем, что магазин добавлен и статус код = 201"):
     assert response_2.status_code == 201
   with allure.step("Проверяем в теле ответа, что имя магазина не пустое"):
     assert response_2.json()["name"] is not None
   with allure.step("Проверяем что, количество элементов в магазине = 0"):
     assert response_2.json()["items"] == 0

 @allure.feature("test_store")
 @allure.story("add_store_wo_auth_header")
 @allure.severity('Normal')
 def test_add_store_wo_auth_header(self):
   with allure.step("Отправляем запрос на добавление информации о юзере"):
     response = UserInformation.add_user_information
     return response
   with allure.step("Отправляем запрос на добавление магазина без заголовка"):
     name_store = Store.add_random_store
     response_2 = requests.post(url=URL+f"{name_store}", headers=None)
   with allure.step("Проверяем, что магазин без заголовка не добавился и статус код = 401"):
     assert response_2.status_code == 401

 @allure.feature("test_store")
 @allure.story("get_store")
 @allure.severity('Normal')
 def test_get_store(self):
   with allure.step("Отправляем запрос на добавление информации о юзере"):
     response = UserInformation.add_user_information
     return response
   with allure.step("Отправляем запрос на получение токена"):
     headers = AuthApp.get_token
   with allure.step("Отправляем запрос на получение информации о магазине"):
     name_store = Store.add_random_store
     response_2 = requests.get(url=URL+f"{name_store}", headers=headers)
   with allure.step("проверяем, что информация получена и статус код = 200"):
     assert response_2.status_code == 200

