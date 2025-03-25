import math

a, b, c = float(input()), float(input()), float(input())
D = (b**2) - 4 * a * c
if a == 0:
    if b != 0:
        print(-c / b)
elif D < 0:
    print("Нет корней")
elif D == 0:
    print(-b / (2 * a))
elif D > 0:
    Ds = math.sqrt(D)
    x_1 = (-b - Ds) / (2 * a)
    x_2 = (-b + Ds) / (2 * a)
    if x_1 > x_2:
        print(x_2, x_1, sep="\n")
    else:
        print(x_1, x_2, sep="\n")
