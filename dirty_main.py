import jmespath
# Пакет для более простого извлечения элементов из JSON-документа

def jmes_1():
    # С помощью подстановочного знака получаем все названия
    d = {"foo": {"bar": [{"name": "one"}, {"name": "two"}]}}
    print(jmespath.search('foo.bar[*].name', d))

def jmes_2():
    # Получаем определенный элемент
    d = {"foo": {"bar": "baz"}}
    print(jmespath.search('foo.bar', d))