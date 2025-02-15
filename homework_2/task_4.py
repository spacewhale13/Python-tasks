"""Задача 4. Строки: Подсчёт символов
Описание: Дана строка. Подсчитайте, сколько раз встречается каждая буква (без учёта регистра) и выведите результат """


def count_elements(line):

    count_letter = [0] * 26
    count_num = [0] * 10

    for element in line.lower():
        if "a" <= element <= "z":
            index_l = ord(element) - ord("a")
            count_letter[index_l] += 1
        elif element.isdigit():
            el = int(element)
            count_num[el] += 1
    for i in range(26):
        print(chr(i + ord("a")), "встречается", count_letter[i], "раз")
    for j in range(10):
        print(j, count_num[j])


count_elements("hry36hffh49h2h3")
