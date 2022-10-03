import pytest
import requests


USERNAME = "test_test123"
PASSWORD = "password321"


@pytest.fixture(scope="module")
def register_user():
    url = "https://stores-tests-api.herokuapp.com/register"
    payload = {"username": USERNAME, "password": None}
    response = requests.post(url=url, json=payload)
    return response


@pytest.fixture(scope="module")
def auth_user_invalid_data():
    url = "https://stores-tests-api.herokuapp.com/auth"
    payload = {"username": USERNAME, "password": "passwor"}
    response = requests.post(url=url, json=payload)
    return response




