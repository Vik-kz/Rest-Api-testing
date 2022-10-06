import pytest
import requests
import allure
from api import Register,UserInformation,AuthApp
from model import RegisterUser,AddUserInfo




class TestUserInfo:
 @allure.feature("test_user_information")
 @allure.story("add_user_info")
 @allure.severity('Critical')
 def test_add_user_info(self):
   with allure.step("Проверяем успешное добавление информации о юзере (POST)"):
    response = UserInformation.add_user_information
    return response
    assert response.status_code == 200
    assert response.json()["message"] == "User info created successfully."

 @allure.feature("test_user_information")
 @allure.story("add_user_info_invalid_user")
 @allure.severity('Normal')
 def test_add_user_info_invalid_user(self):
   with allure.step("Проверяем добавление информации о юзере c несуществующем id (POST)"):
     response = UserInformation.add_user_none_exist
     return response
     assert response.status_code == 404
     assert response.json()["message"] == "User not found"

 @allure.feature("test_user_information")
 @allure.story("get_user_info")
 @allure.severity('Critical')
 def test_get_user_info(self):
   with allure.step("Проверяем получение существующей информации о юзере (GET)"):
     response = UserInformation.get_user_information
     return response
     assert response.status_code == 200

