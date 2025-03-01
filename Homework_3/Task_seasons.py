def seasons(season, months_num):
    for month, months in season.items():
        if months_num in months:
            return month


season = {
    "Зима": [12, 1, 2],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8],
    "Осень": [9, 10, 11],
}


months_num = int(input())
print(seasons(season, months_num))
