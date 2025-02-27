import pytest

@pytest.fixture  # переопределение фикстуры
def api_key():
    return "LOAD-API-KEY-98765"

@pytest.fixture  # для лоад тестов
def load_test_info():
    return {"load_factor": 1000}