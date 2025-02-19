"""На вход программе подаётся строка текста, содержащая различные натуральные числа. 
Вам необходимо переставить максимальный и минимальный элементы местами и вывести изменённую строку."""


def changing_index(s):
    s1 = [int(i) for i in s]
    min_el = s1.index(min(s1))
    max_el = s1.index(max(s1))
    s1[min_el], s1[max_el] = s1[max_el], s1[min_el]
    s2 = [str(j) for j in s1]
    return " ".join(s2)


result = changing_index(input().split())

print(result)
