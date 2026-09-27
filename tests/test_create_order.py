import allure

from api import StellarBurgersApi
from data.ingredients_data import Ingredient


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user):
        api = StellarBurgersApi()
        token = create_user[3]

        response = api.create_order(
            payload=Ingredient.correct_ingredients_data,
            token=token
        )

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа неавторизованным пользователем")
    def test_create_order_not_auth(self):
        api = StellarBurgersApi()

        response = api.create_order(
            payload=Ingredient.correct_ingredients_data
        )

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        api = StellarBurgersApi()

        response = api.create_order()

        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидным хешем ингредиента")
    def test_create_order_invalid_hash_ingredient(self):
        api = StellarBurgersApi()

        response = api.create_order(
            payload=Ingredient.incorrect_ingredients_data
        )

        assert response.status_code == 500
        assert "Internal Server Error" in response.text
