"""Задача 7. Переменные, списки: Распаковка последовательностей
Описание: Создайте список из трёх элементов, распакуйте его в отдельные переменные и выведите каждую переменную."""


def unpacking_elements(list_elements):
    a, b, c = list_elements

    return a, b, c


list_elements = [2, 3, 4]

result = unpacking_elements(list_elements)
print(result)
