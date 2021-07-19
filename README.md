Pytest demo!

Щоб проєкт поставився з тестовим середовищем:

```pip install -e .[test]```

Рахувати code coverage:

```pytest --cov=our_namespace.pytest_demo tests/```

Показати результати детально і 3 найповільніші тести:

```pytest --durations=3 -vv```

Показати print з тестів (за умовчанням їх не видно, якщо тест проходить):

```pytest --capture=no```