import allure

from data.ingredients_data import Ingredient


@allure.suite("Получение заказов пользователя")
class TestGetOrderUser:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_order_user_with_auth(self, api, create_user):
        token = create_user[3]

        create_response = api.create_order(
            payload=Ingredient.correct_ingredients_data,
            token=token
        )

        get_response = api.get_user_orders(token)

        assert get_response.status_code == 200
        assert (
            get_response.json()["orders"][0]["number"]
            == create_response.json()["order"]["number"]
        )

    @allure.title("Получение заказов без авторизации")
    def test_get_order_user_not_auth(self, api):
        response = api.get_user_orders("")

        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
