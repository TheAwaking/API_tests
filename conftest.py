import pytest
import random

@pytest.fixture  #  доступно для всех тестов
def random_number():
    return random.randint(1, 100)