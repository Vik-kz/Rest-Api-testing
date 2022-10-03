import requests
from model import RegisterUser,AddUserInfo,Store

URL = "https://stores-tests-api.herokuapp.com"

class Register:
    def __init__(self,url):
        self.url = url


    POST_REGISTER = '/register'

    def register_user(self, body: dict):
     """
     https://stores-tests-api.herokuapp.com/register
     """
     return requests.post(f"{self.url}{self.POST_REGISTER}", json=body)

    def register_app_user(self):
      body = RegisterUser.random()
      response = Register(url=URL).register_user(data=body)
      return response


    def auth_app_user(self):
      url = "https://stores-tests-api.herokuapp.com/auth"
      data = register_app_user
      response = requests.post(url=url, data=data)
      return response.json()["access_token"]

class AuthApp:
    def get_token(self):
      response = Register.register_app_user
      return response
      token = Register.auth_app_user
      header = {"Authorization": f"JWT {token}"}
      return header



class UserInformation:
    def add_user_information(self):
      url = "https://stores-tests-api.herokuapp.com/user_info"
      data = AddUserInfo.random_user_info()
      headers = AuthApp.get_token()
      response = requests.post(url=url, data=data, header=headers)
      return response

    def add_user_none_exist(self):
      url = "https://stores-tests-api.herokuapp.com/user_info"
      headers = AuthApp.get_token()
      none_exist_user = "/1000"
      response = requests.post(url=url+f"{none_exist_user}", headers=headers)
      return response

    def get_user_information(self):
      url = "https://stores-tests-api.herokuapp.com/user_info"
      headers = AuthApp.get_token()
      none_exist_user = "/1"
      response = requests.post(url=url+f"{none_exist_user}", headers=headers)