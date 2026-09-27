import allure

from api import StellarBurgersApi
from data.user_data import User


@allure.suite("Авторизация пользователя")
class TestLogin:

    @allure.title("Авторизация существующего пользователя")
    def test_login_user(self, create_user):
        api = StellarBurgersApi()

        login_data = create_user[2]

        response = api.login_user(login_data)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Авторизация с некорректным логином и паролем")
    def test_login_user_error(self):
        api = StellarBurgersApi()

        response = api.login_user(User.data_negative)

        assert response.status_code == 401
        assert response.json().get("success") is False
