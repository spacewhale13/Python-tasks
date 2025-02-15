def binary_search(num, target):
    left = 0
    right = len(num) - 1

    while left <= right:

        middle = (right + left) // 2
        if num[middle] < target:
            left = middle + 1

        elif num[middle] > target:
            right = middle - 1

        elif num[middle] == target:

            return num[middle]

    return "Ошибка"


num = [1, 2, 3]
target = 2
if binary_search(num, target) == "Ошибка":
    print("Элемент не найден")
else:
    print(binary_search(num, target))


"""Дан отсортированный список чисел и целевое число target. Тебе нужно найти число в списке, которое ближе всего к target."""


def closet_search(num, target):
    left = 0
    right = len(num) - 1
    closet = num[0]

    while left <= right:

        middle = (right + left) // 2
        if (target - num[middle]) > (target - num[0]):
            closet = num[middle]
            if (target - num[middle]) == (target - closet):
                return min(closet, num[middle])

    return "Ошибка"


num = [1, 2, 3, 16, 389, 489]
target_1 = 4
if closet_search(num, target) == "Ошибка":
    print("Элемент не найден")
else:
    print(binary_search(num, target))
