"""Задача 1. Списки: Модификация элементов
Описание: Создайте список чисел, измените значение второго элемента и добавьте новый элемент в конец списка.
"""


def modification_list(numbers, new_element):
    numbers[1] = 25
    numbers.append(new_element)

    return numbers


if __name__ == "__main__":
    modification_list([12, 3453, 45, 46, 352], 2345)
