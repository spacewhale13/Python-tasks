""" Строки: Анализ текста
Описание: Напишите программу, которая принимает текст, подсчитывает количество слов, количество символов без пробелов и частоту встречаемости каждого слова."""


def analys_text(text):

    count_words = len(text.split())
    count_symbols = len(text.replace(" ", ""))
    return count_words, count_symbols


text = "Напишите программу, которая принимает текст, подсчитывает количество слов."
count_words, count_symbols = 0, 0
result = analys_text(text)
print(result)
