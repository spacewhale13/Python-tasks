"""Задача 2. Строки: Срезы
Описание: Дана строка. выведите с 4 по 10 символы, если это не возможно, дайте знать это"""


def print_string(line):
    if len(line) >= 10:
        print(line[4:11])
    else:
        print("No god")
    return line


print_string("ethnxrfmrmr,mr,mxu")
