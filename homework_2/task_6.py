<<<<<<< HEAD
s = input()
pair = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            pair += 1
print(pair)        
=======
"""Задача 6. Переменные, списки: Обмен значений
Описание: Напишите программу, которая меняет местами значения двух переменных с использованием распаковки списка."""


def swap_values(values):
    values[0], values[1] = values[1], values[0]
    return values


values = [5, 3]

print(values)
swap_values(values)
print(*values, sep=", ")
>>>>>>> de8b46c386c5496f5f8adeb5ee10c13a723663b9
