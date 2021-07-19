import pytest

"""https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files
Тут пишуть, що pytest автоматично буде знаходити всі conftest.py і навіть імпортувати їх не треба. 
Тобто всі fixture звідси будуть доступні в інших файлах. 
Але реально так працювати не дуже зручно, бо IDE лається."""


def pytest_make_parametrize_id(config, val):
    """Hook для валідного відображення кирилиці у pytest"""
    return repr(val)


def print_(*args, **kwargs):
    """Можемо закоментувати цей рядок, якщо хочемо прибрати всі виклики print."""
    print(*args, **kwargs)


# session-scope fixtures
