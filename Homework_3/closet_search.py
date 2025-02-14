"""Дан отсортированный список чисел и целевое число target. Тебе нужно найти число в списке, которое ближе всего к target."""


def closet_search(num, target):
    left = 0
    right = len(num) - 1
    closet = num[0]

    while left <= right:

        middle = (right + left) // 2
        if abs(target - num[middle]) > abs(target - closet):

            closet = num[middle]
        elif abs(target - num[middle]) < abs(target - closet):

            closet = num[middle]

        elif abs(target - num[middle]) == abs(target - closet):
            return min(closet, num[middle])

        if num[middle] > target:
            right = middle - 1
        if num[middle] < target:
            left = middle + 1

    return closet


num = [1, 3, 5, 16, 389, 489]
target = 4
print(closet_search(num, target))


"""Дан отсортированный список чисел и целевое число target. Нужно найти две такие числа в списке, сумма которых наиболее близка к target."""


def closet_sum(num, target):
    left = 0
    right = len(num) - 1
    current_sum = num[left] + num[right]
    final_sum = float("inf")
    best_numbers = (num[left], num[right])
    if current_sum == target:
        return current_sum
    if abs(current_sum - target) < (final_sum - target):
        final_sum = current_sum
        best_pair = (num[left], num[right])
    elif current_sum > target:
        right -= 1
    elif current_sum < target:
        left += 1

    return best_pair


num = [1, 3, 5, 16, 389, 489]
target = 4
print(closet_sum(num, target))
