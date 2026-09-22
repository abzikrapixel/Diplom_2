from faker import Faker
from uuid import uuid4


class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        return {
            "email": f"test_{uuid4().hex}@example.com",
            "password": fake.password(),
            "name": fake.name()
        }

    data_correct = {
        "email": "tets_2503@yandex.ru",
        "password": "password"
    }

    data_negative = {
        "email": "tets_2503123@yandex.ru",
        "password": "password"
    }

    data_double = {
        "email": "tets_2503@yandex.ru",
        "password": "password",
        "name": "Username"
    }

    data_without_email = {
        "email": "",
        "password": "password",
        "name": "Username"
    }

    data_without_password = {
        "email": "tets_2503@yandex.ru",
        "password": "",
        "name": "Username"
    }

    data_without_name = {
        "email": "tets_2503@yandex.ru",
        "password": "password",
        "name": ""
    }

    data_updated = {
        "email": "tets_2503@yandex.ru",
        "password": "password",
        "name": "Test"
    }
