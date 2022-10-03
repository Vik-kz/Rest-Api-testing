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
   with allure.step("Отправляем запрос на добавление информации о юзере"):
    response = UserInformation.add_user_information
    return response
   with allure.step("Проверяем, что статус код = 200"):
    assert response.status_code == 200
   with allure.step("Проверяем сообщение в теле ответа, что информация успешно добавлена"):
    assert response.json()["message"] == "User info created successfully."

 @allure.feature("test_user_information")
 @allure.story("add_user_info_invalid_user")
 @allure.severity('Normal')
 def test_add_user_info_invalid_user(self):
   with allure.step("Отправляем запрос на добавление информации c несуществующем id юзера"):
     response = UserInformation.add_user_none_exist
     return response
   with allure.step("Проверяем, что статус код = 404"):
     assert response.status_code == 404
   with allure.step("Проверяем в теле ответа сообщение о том, что юзер не найден"):
     assert response.json()["message"] == "User not found"

 @allure.feature("test_user_information")
 @allure.story("get_user_info")
 @allure.severity('Critical')
 def test_get_user_info(self):
   with allure.step("Отправляем запрос на получение информации о юзере"):
     response = UserInformation.get_user_information
     return response
   with allure.step("Проверяем, что информация получена и статус код = 200"):
     assert response.status_code == 200

