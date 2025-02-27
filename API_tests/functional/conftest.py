import pytest

@pytest.fixture #  для функциональных апи тестов
def user_info():
    return {"username": "test_user", "password": "secure_password"}