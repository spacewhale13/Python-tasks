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
