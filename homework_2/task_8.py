<<<<<<< HEAD
""" Строки: Анализ текста
Описание: Напишите программу, которая принимает текст, подсчитывает количество слов, количество символов без пробелов и частоту встречаемости каждого слова."""


def analys_text(text):

    count_words = len(text.split())
    count_symbols = len(text.replace(" ", ""))
    print(count_words, count_symbols)


text = "Напишите программу, которая принимает текст, подсчитывает количество слов."
count_words, count_symbols = 0, 0
analys_text(text)
=======
""" Строки: Анализ текста
Описание: Напишите программу, которая принимает текст, подсчитывает количество слов, количество символов без пробелов и частоту встречаемости каждого слова."""


def analys_text(text):

    count_words = len(text.split())
    count_symbols = len(text.replace(" ", ""))
    print(count_words, count_symbols)


text = "Напишите программу, которая принимает текст, подсчитывает количество слов."
count_words, count_symbols = 0, 0
analys_text(text)
>>>>>>> de8b46c386c5496f5f8adeb5ee10c13a723663b9
