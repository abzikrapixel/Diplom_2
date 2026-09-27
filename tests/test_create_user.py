import allure
import pytest

from api import StellarBurgersApi
from data.user_data import User


@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        api = StellarBurgersApi()
        payload = User.create_data_user()

        response = api.create_user(payload)

        assert response.status_code == 200
        assert response.json().get("success") is True

        token = response.json()["accessToken"]
        api.delete_user(token)

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self, create_user):
        api = StellarBurgersApi()

        payload = create_user[1]

        response = api.create_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @pytest.mark.parametrize(
        "payload",
        [
            User.data_without_email,
            User.data_without_password,
            User.data_without_name,
        ],
        ids=[
            "без email",
            "без password",
            "без name",
        ],
    )
    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_without_required_field(self, payload):
        api = StellarBurgersApi()

        response = api.create_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
