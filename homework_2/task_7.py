"""Задача 7. Переменные, списки: Распаковка последовательностей
Описание: Создайте список из трёх элементов, распакуйте его в отдельные переменные и выведите каждую переменную."""


def unpacking_elements(list_elements):
    for i in list_elements:
        print(i, end=" ")
    print()


list_elements = [2, 3, 4]

unpacking_elements(list_elements)
