from typing import Union


def add_simple(a: Union[int, float], b: Union[int, float]) -> float:
    """Проста функція, зрозуміла поведінка. Сума двох чисел.

    :param a: Union[int, float]
        Доданок 1.
    :param b: Union[int, float]
        Доданок 2.
    :return: Сума a та b.
    :rtype: float
    """
    return float(a + b)


def add_all(*args, **kwargs) -> float:
    """
    Складніша функція. Рахує суму всіх аргументів.
    :param args: Аргументи, суму яких треба порахувати.
    :param kwargs: Може опціонально містити іменований параметр debug: dict. Якщо цей параметр передано,
        за ключем "add_all" вносить інформацію про роботу методу.
    :return: Сума аргументів.
    :raises:
        ValueError: Якщо якийсь з аргументів не належить до типу float або int.
    """
    if not all([(type(x) is float) or (type(x) is int) for x in args]):
        raise ValueError("Arguments should be int or float.")
    if kwargs and (debug := kwargs.get("debug")) is not None:
        add_all_info = debug.get("add_all") or []
        add_all_info.append(args)
        debug["add_all"] = add_all_info
    return float(sum(args))
