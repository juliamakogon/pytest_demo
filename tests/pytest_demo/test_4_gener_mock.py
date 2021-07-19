from .conftest import *

from our_namespace.pytest_demo.gener import *
from our_namespace.pytest_demo.add import *

"""
-----------------------------------
Залежності та випадковості.
-----------------------------------
monkeypatch: Модифікуємо поведінку об'єкта
https://docs.pytest.org/en/6.2.x/monkeypatch.html
Mock: об'єкт, який імітує поведінку "залежності"
pytest-mock: 
https://changhsinlee.com/pytest-mock/
https://medium.com/analytics-vidhya/mocking-in-python-with-pytest-mock-part-i-6203c8ad3606
"""

GENER_PARAMS = [(0, 0), (1, 2), (2, 1.5), (4, 6)]


class TestNumGenerator:
    """Тестуємо інтеграцію NumGenerator та функції add_all"""

    @pytest.fixture(scope="class", params=GENER_PARAMS)
    def gener(self, request):
        count_, sum_ = request.param
        return NumGenerator(count=count_, sum=sum_)

    def test_add(self, gener):
        expected = gener.sum
        values = list(gener)
        print_(repr(self), values)
        actual = add_all(*values)
        assert actual == pytest.approx(expected)


class TestRandGenerator(TestNumGenerator):
    """Тестуємо клас, який повертає щоразу випадкову послідовність.
    Тести успадкуються від базового класу, але ми перевизначаємо fixture."""

    @pytest.fixture(scope="class", params=GENER_PARAMS)
    def gener(self, request):
        numpy = pytest.importorskip("numpy")  # TODO: test it :)
        count_, sum_ = request.param
        return RandGenerator(count=count_, sum=sum_)


class TestRandGeneratorPatched(TestRandGenerator):
    """Хочемо позбутися залежності від генератора випадкових чисел з допомогою monkeypatch."""

    class MonkeyRng:
        def random(self):
            return 0.5

    @pytest.fixture(autouse=True)
    def patching(self, monkeypatch):
        monkeypatch.setattr("our_namespace.pytest_demo.gener.RandGenerator.rng", self.MonkeyRng())

    def test_random_is_killed(self, gener):
        assert list(gener) == list(gener)
