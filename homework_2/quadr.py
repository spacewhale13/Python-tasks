from math import *

a, b, c = float(input()), float(input()), float(input())
D = (b**2) - 4 * a * c
D_sqrt = sqrt(D)
if a == 0:
    if b != 0:
        print(-c / b)
elif D < 0:
    print("Нет корней")
elif D == 0:
    print(-b / (2 * a))
elif D > 0:
    print((-b - D_sqrt) / (2 * a), (-b + D_sqrt) / (2 * a), sep="\n")
