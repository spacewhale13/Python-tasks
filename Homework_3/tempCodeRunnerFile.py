"""Дан отсортированный список чисел и целевое число target. Тебе нужно найти число в списке, которое ближе всего к target."""


def closet_search(num, target):
    left = 0
    right = len(num) - 1
    closet = num[0]

    while left <= right:

        middle = (right + left) // 2
        if abs(target - num[middle]) > abs(target - closet):
            closet = num[middle]
            left = middle + 1
        elif abs(target - num[middle]) < abs(target - closet):
            closet = num[middle]
            right = middle - 1

        elif (target - num[middle]) == (target - closet):
            return min(closet, num[middle])


num = [1, 3, 5, 16, 389, 489]
target = 4
print(closet_search(num, target))
