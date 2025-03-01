def seasons(season, months_num):

    if months_num.isdigit():
        if 1 <= int(months_num) <= 12:
            for month, months in season.items():
                if int(months_num) in months:
                    return month
    if months_num.isalpha():
        return "Вы ввели буквы"

    for i in months_num:
        if i in "!@#$%^&*()_+=-:;|\/":
            return "Вы ввели неправильные символы"


season = {
    "Зима": [12, 1, 2],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8],
    "Осень": [9, 10, 11],
}
months_num = input()

print(seasons(season, months_num))
