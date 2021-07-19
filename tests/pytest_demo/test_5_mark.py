from .conftest import *
from itertools import chain

from our_namespace.pytest_demo.gener import *
from our_namespace.pytest_demo.add import *

"""
Мітки класів можуть додавати користувачі.
Див. pytest.ini
https://docs.pytest.org/en/6.2.x/example/markers.html#mark-examples

"""


@pytest.mark.slow()
def test_slow():
    """Це може бути повільний тест.
    Щоб запустити всі крім повільних:
    pytest -m "not slow"
    """
    gener = RandGenerator(count=10000, sum=10.2)
    actual = add_all(*gener)
    assert actual == pytest.approx(gener.sum)


@pytest.mark.smoke()
def test_sanity():
    """Це можуть бути тести для перевірки системи в цілому. Запустити лише їх:
     pytest -m smoke
     """
    gener1 = NumGenerator(count=100, sum=10.2)
    gener2 = RandGenerator(count=50, sum=20.1)
    actual = add_all(*chain(gener1, gener2))
    assert actual == pytest.approx(30.3)
