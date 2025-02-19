"""На вход программе подаётся строка текста, содержащая целые числа. Из данной строки формируется список чисел. 
Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать."""


def counting_pairs(s, pair):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                pair += 1
    return pair


result = counting_pairs(input().split(" "), 0)
print(result)
