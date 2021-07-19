from .conftest import *
from our_namespace.pytest_demo.add import *

"""
-------------------------------------------
Базові тести та параметризовані тести.
-------------------------------------------
"""


def test_add_simple_two_ints(a=1, b=2, expected=3):
    """Найпростіший тест, зверніть увагу на порядок в assert."""
    actual = add_simple(a, b)
    assert actual == expected


def test_add_simple_two_floats(a=1.5, b=2.5, expected=4.0001):
    """Тест для демонстрації approx."""
    actual = add_simple(a, b)
    assert actual == pytest.approx(expected, rel=1e-4)


@pytest.mark.xfail(reason="Для демонстрації xfail.")
def test_add_simple_two_str(a="1", b="2", expected=3):
    """Тест для демонстрації xfail та повідомлень assert."""
    actual = add_simple(a, b)
    assert actual == expected, "Додали два рядки."


@pytest.mark.parametrize("a, b, expected",
                         [(1, 2, 3),
                          (1.5, 2.5, 4.0001),
                          pytest.param("1", "2", None, marks=pytest.mark.xfail)])
def test_add_simple_when_two_args(a, b, expected):
    """Параметризований тест"""
    actual = add_simple(a, b)
    assert actual == pytest.approx(expected, rel=1e-4)


@pytest.mark.parametrize("a, b, expected",
                         [(1, 2, 3),
                          (1.5, 2.5, 4.0001),
                          pytest.param("1", "2", None, marks=pytest.mark.xfail)])
def test_add_all_when_two_args(a, b, expected):
    """Параметризований тест"""
    actual = add_all(a, b)
    assert actual == pytest.approx(expected, rel=1e-4)


@pytest.mark.parametrize("args, expected",
                         [((), 0),  # corner case 1
                          ((11.1,), 11.1),  # corner case 2
                          ((1, 2), 3),
                          ((1.5, 2.5), 4.0001),
                          ((1.5, 2.5, 2.1), 6.1),
                          pytest.param(("1", "2"), None, marks=pytest.mark.xfail)])
def test_add_all_when_many_args(args, expected):
    """Параметризований тест."""
    actual = add_all(*args)
    assert actual == pytest.approx(expected, rel=1e-4)


@pytest.mark.parametrize("args",
                         [("1", 2),
                          (1.5, "2"),
                          (1.5, 0, "2")])
def test_add_all_raises_exception(args):
    """Код мусить видати виключення через неправильні параметри методу.
    https://docs.pytest.org/en/6.2.x/assert.html#assertions-about-expected-exceptions"""
    with pytest.raises(ValueError):
        add_all(*args)


"""Тестуємо параметр debug, потрібний для grey box testing."""


@pytest.fixture(scope="module")
def debug_obj():
    return {}


@pytest.mark.parametrize("args, expected",
                         [((), 0),  # corner case 1
                          ((11.1,), 11.1),  # corner case 2
                          ((1, 2), 3),
                          ((1.5, 2.5), 4.0001),
                          ((1.5, 2.5, 2.1), 6.1)])
def test_add_all_when_debug_not_isolated(debug_obj, args, expected):
    """Це також приклад тесту, який порушує правило ізоляції:
    значення debug_obj буде залежати від того, які тести запускалися. Так робити НЕ ТРЕБА :)"""
    add_all(*args, debug=debug_obj)
    assert debug_obj.get("add_all")
    print_(debug_obj)


def test_add_all_when_debug():
    """Це приклад тесту, який НЕ порушує правило ізоляції."""
    debug_obj = {}
    params = [(1, 2), (1.5, 2.5)]
    for args in params:
        add_all(*args, debug=debug_obj)
        print_(debug_obj)
    assert debug_obj.get("add_all")
    assert len(debug_obj["add_all"]) == len(params)
