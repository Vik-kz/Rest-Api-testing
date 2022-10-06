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
   with allure.step("Проверяем успешное добавление магазина (POST)"):
     response = UserInformation.add_user_information
     return response
     headers = AuthApp.get_token
     name_store = Store.add_random_store
     response_2 = requests.post(url=URL+f"{name_store}", headers=headers)
     return response_2
     assert response_2.status_code == 201
     assert response_2.json()["name"] is not None
     assert response_2.json()["items"] == 0

 @allure.feature("test_store")
 @allure.story("add_store_wo_auth_header")
 @allure.severity('Normal')
 def test_add_store_wo_auth_header(self):
   with allure.step("Проверяем добавление магазина без заголовка к запросу (POST)"):
     response = UserInformation.add_user_information
     return response
     name_store = Store.add_random_store
     response_2 = requests.post(url=URL+f"{name_store}", headers=None)
     assert response_2.status_code == 401

 @allure.feature("test_store")
 @allure.story("get_store")
 @allure.severity('Normal')
 def test_get_store(self):
   with allure.step("Проверяем получение информации о магазине (GET)"):
     response = UserInformation.add_user_information
     return response
     headers = AuthApp.get_token
     name_store = Store.add_random_store
     response_2 = requests.get(url=URL+f"{name_store}", headers=headers)
     assert response_2.status_code == 200

