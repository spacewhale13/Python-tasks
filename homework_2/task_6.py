"""Задача 6. Переменные, списки: Обмен значений
Описание: Напишите программу, которая меняет местами значения двух переменных с использованием распаковки списка."""


def swap_values(values):
    values[0], values[1] = values[1], values[0]
    return values


values = [5, 3]

print(values)
swap_values(values)
print(*values, sep=", ")
