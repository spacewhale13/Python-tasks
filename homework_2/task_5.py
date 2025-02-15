"""Задача 5. Списки: Сортировка
Описание: Создайте список строк (например, имена) и отсортируйте его по алфавиту."""


def sort_names(name):

    return sorted(name)


name = ["Катя", "Маша", "Паша", "Лена", "Макс"]
sorted_names = sort_names(name)


print(sorted_names)
