import pytest

@pytest.fixture #  для ui тестов
def browser():
    return "Chrome"