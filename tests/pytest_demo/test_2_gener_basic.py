from .conftest import *
from our_namespace.pytest_demo.gener import NumGenerator

'''
------------------------------------------------------------------------------
В цьому файлі: найпростіші fixture, коли використовувати skip або xfail.
------------------------------------------------------------------------------
https://docs.pytest.org/en/6.2.x/fixture.html
Стадії тесту. 
https://docs.pytest.org/en/6.2.x/fixture.html#what-fixtures-are
Test:
1. Arrange == fixture
2. Act
3. Assert
4. Cleanup == yield fixture, вивільнення ресурсів (закриття файлу абощо), 
    див. https://docs.pytest.org/en/6.2.x/fixture.html#teardown-cleanup-aka-fixture-finalization
'''


@pytest.fixture(scope="module")
# Існує в межах одного модуля, default: scope=function, всі можливі варіанти:
# function, class, module, package, session
def num_generator_10_2():
    # 1. Arrange
    return NumGenerator(10, 2.)


def test_num_generator_10_2(num_generator_10_2):
    # 2. Act
    s = 0
    i = 0
    for a in num_generator_10_2:
        s += a
        i += 1
    # 3. Assert
    assert i == num_generator_10_2.count
    assert s == pytest.approx(num_generator_10_2.sum)


# fixtures can use other fixtures
@pytest.fixture()  # scope=function, створюється перед кожним запуском тесту, може
def num_generator_10_2_count_faked(num_generator_10_2):
    return num_generator_10_2.count + 1


"""Пропускаємо тести https://docs.pytest.org/en/6.2.x/skipping.html:
Можна пропустити в цілому файлі з допомогою allow_module_level=True 
або з допомогою https://docs.pytest.org/en/6.2.x/skipping.html#summary
+ якщо вони неправильно сконфігуровані
+ якщо немає потрібної компоненти
+ якщо тестуємо на іншій платформі
+ якщо неможливо імпортувати модуль importorskip"""


def test_num_generator_10_2_skip1(num_generator_10_2, num_generator_10_2_count_faked):
    if num_generator_10_2_count_faked != num_generator_10_2.count:
        pytest.skip("Треба перевірити дизайн тестів, дані для тестів підготовлені неправильно")
    assert True


@pytest.mark.skip(reason="Цей тест застарів")
def test_num_generator_10_2_skip2(num_generator_10_2, num_generator_10_2_count_faked):
    assert True


@pytest.mark.skipif('''sys.platform != "win32"''', reason="tests for windows only")
def test_num_generator_10_2_skipif1(num_generator_10_2, num_generator_10_2_count_faked):
    assert True


@pytest.mark.skipif('''sys.platform == "win32"''', reason="tests not for windows")
def test_num_generator_10_2_skipif2(num_generator_10_2, num_generator_10_2_count_faked):
    assert True


@pytest.mark.xfail(reason="Ми знаємо, що цей тест падає, і знаємо причину, тому наразі фіксуємо, але не фіксимо.")
def test_num_generator_10_2_xfail(num_generator_10_2, num_generator_10_2_count_faked):
    assert num_generator_10_2_count_faked == num_generator_10_2.count


@pytest.mark.xfail(
    reason="Ми знаємо, що цей тест падає, і знаємо причину, тому наразі фіксуємо, але не фіксимо. Навіть запускати його не будемо.",
    run=False)
def test_num_generator_10_2_xfail2(num_generator_10_2, num_generator_10_2_count_faked):
    assert num_generator_10_2_count_faked == num_generator_10_2.count


@pytest.mark.xfail(reason="Цей тест точно впаде, бо в ньому pytest.fail.")
def test_fail():
    pytest.fail("Тест впав, як і обіцяли.")
