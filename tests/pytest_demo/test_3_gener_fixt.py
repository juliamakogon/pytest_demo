from .conftest import *

from our_namespace.pytest_demo.gener import *

"""
------------------------------------------------
Досліджуємо більш складні варіанти fixture:
------------------------------------------------
1. Передаємо параметри через mark
https://docs.pytest.org/en/6.2.x/fixture.html#using-markers-to-pass-data-to-fixtures
"""

"""
2. Параметризація fixture - всі тести автоматично стають параметризованими
    https://docs.pytest.org/en/6.2.x/fixture.html#parametrizing-fixtures
Можна разом з цим використовувати params:
@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
"""


@pytest.fixture(scope="module", params=[0, 1, 2.5])
def num_generator_sum(request):
    s = request.param
    return s


@pytest.fixture(scope="module", params=[0, 1, 2, 10])
def num_generator_parametrized(request, num_generator_sum):
    count = request.param
    return NumGenerator(count=count, sum=num_generator_sum)


def test_num_generator_parametrized(num_generator_parametrized):
    """Це тест, параметризований автоматично через fixture."""
    # 2. Act
    s = 0
    i = 0
    for a in num_generator_parametrized:
        s += a
        i += 1
    # 3. Assert
    assert i == num_generator_parametrized.count
    if num_generator_parametrized.count > 0:
        assert s == pytest.approx(num_generator_parametrized.sum)


"""
Автоматичне використання fixture

a) https://docs.pytest.org/en/6.2.x/fixture.html#autouse-fixtures-fixtures-you-don-t-have-to-request
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)

b) https://docs.pytest.org/en/6.2.x/fixture.html#use-fixtures-in-classes-and-modules-with-usefixtures
and you may specify fixture usage at the test module level using pytestmark:

@pytest.mark.usefixtures("cleandir", "anotherfixture")
def test():
...

На рівні всього файлу
pytestmark = pytest.mark.usefixtures("cleandir")

It is also possible to put fixtures required by all tests in your project into an ini-file:
# content of pytest.ini
[pytest]
usefixtures = cleandir
"""

"""
Fixture можна перевизначати
https://docs.pytest.org/en/6.2.x/fixture.html#overriding-fixtures-on-various-levels
"""
