import pytest

from api import StellarBurgersApi
from data.user_data import User


@pytest.fixture
def api():
    return StellarBurgersApi()


@pytest.fixture(scope="function")
def create_user():
    api = StellarBurgersApi()

    payload = User.create_data_user()
    login_data = {
        "email": payload["email"],
        "password": payload["password"]
    }

    response = api.create_user(payload)

    if response.status_code != 200:
        pytest.fail(
            f"Не удалось подготовить пользователя. "
            f"Status: {response.status_code}, Response: {response.text}"
        )

    token = response.json()["accessToken"]

    yield response, payload, login_data, token

    api.delete_user(token)


@pytest.fixture(scope="function")
def unique_user():
    api = StellarBurgersApi()
    payload = User.create_data_user()

    response = api.create_user(payload)

    if response.status_code != 200:
        pytest.fail(
            f"Не удалось создать пользователя. "
            f"Status: {response.status_code}, Response: {response.text}"
        )

    token = response.json()["accessToken"]

    yield response

    api.delete_user(token)
