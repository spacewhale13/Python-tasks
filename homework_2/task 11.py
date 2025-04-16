"""На вход программе подаётся строка текста, содержащая различные натуральные числа.
Вам необходимо переставить максимальный и минимальный элементы местами и вывести изменённую строку.
Ограничение на длину строки 10^9
"""

"""s1 = [int(i) for i in s]
    min_el = s1.index(min(s1))
    max_el = s1.index(max(s1))
    s1[min_el], s1[max_el] = s1[max_el], s1[min_el]
    s2 = [str(j) for j in s1]
    return " ".join(s2)"""


def changing_index(s):
    if not s:
        return s

    min_el = 10e9 + 1
    max_el = 0
    min_i, max_i = 0, 0
    s1 = s.split()
    for i, el in enumerate(s1):
        num = int(el)

        if max_el < num:
            max_el = num
            max_i = i
        if min_el > num:
            min_el = num
            min_i = i

    s1[max_i], s1[min_i] = s1[min_i], s1[max_i]
    print(min_i, max_i)
    return " ".join(s1)


if __name__ == "__main__":
    input_str = "1 "
    result = changing_index(input_str)

print(result)
