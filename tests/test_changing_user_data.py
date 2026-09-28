import allure

from data.user_data import User


@allure.suite("Изменение данных пользователя")
class TestChangingUserData:

    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_changing_user_email_with_auth(self, api, create_user):
        token = create_user[3]

        payload = {
            "email": User.create_data_user()["email"]
        }

        response = api.change_user_data(token, payload)

        assert response.status_code == 200
        assert response.json()["user"]["email"] == payload["email"]

    @allure.title("Успешное изменение пароля авторизованного пользователя")
    def test_changing_user_password_with_auth(self, api, create_user):
        token = create_user[3]

        payload = {
            "password": User.create_data_user()["password"]
        }

        response = api.change_user_data(token, payload)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Успешное изменение имени авторизованного пользователя")
    def test_changing_user_name_with_auth(self, api, create_user):
        token = create_user[3]

        payload = {
            "name": User.create_data_user()["name"]
        }

        response = api.change_user_data(token, payload)

        assert response.status_code == 200
        assert response.json()["user"]["name"] == payload["name"]

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_not_auth(self, api):
        response = api.change_user_data(
            token="",
            payload=User.create_data_user()
        )

        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
