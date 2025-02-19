"""Задача 2. Строки: Срезы
Описание: Дана строка. выведите с 4 по 10 символы, если это не возможно, дайте знать это"""


def print_string(line):
    if len(line) >= 10:
        return line[4:11]
    else:
        return None


new_line = print_string("aeh")
print(new_line)
