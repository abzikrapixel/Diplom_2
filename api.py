import allure
import requests

from data.handlers import Urls, Handlers


class StellarBurgersApi:

    @allure.step("Создать пользователя")
    def create_user(self, payload):
        return requests.post(
            f"{Urls.MAIN_URL}{Handlers.CREATE_USER}",
            json=payload
        )

    @allure.step("Авторизовать пользователя")
    def login_user(self, payload):
        return requests.post(
            f"{Urls.MAIN_URL}{Handlers.LOGIN}",
            json=payload
        )

    @allure.step("Удалить пользователя")
    def delete_user(self, token):
        return requests.delete(
            f"{Urls.MAIN_URL}{Handlers.DELETE_USER}",
            headers={"Authorization": token}
        )

    @allure.step("Изменить данные пользователя")
    def change_user_data(self, token, payload):
        return requests.patch(
            f"{Urls.MAIN_URL}{Handlers.CHANGE_USER_DATA}",
            headers={"Authorization": token},
            json=payload
        )

    @allure.step("Создать заказ")
    def create_order(self, payload=None, token=None):
        headers = {}

        if token:
            headers["Authorization"] = token

        return requests.post(
            f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}",
            headers=headers,
            json=payload
        )

    @allure.step("Получить заказы пользователя")
    def get_user_orders(self, token):
        return requests.get(
            f"{Urls.MAIN_URL}{Handlers.GET_ORDERS}",
            headers={"Authorization": token}
        )
