a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())
if (a1 == a2 and abs(b1 - b2) == 1 or b1 == b2 and abs(a1 - a2) == 1) and (
    (a2 == a1 - 1 and b2 == b1 - 1)
    or (a2 == a1 + 1 and b2 == b1 - 1)
    or (a2 == a1 + 1 and b2 == b1 + 1)
    or (a2 == a1 - 1 and b2 == b1 + 1)
):
    print("YES")
else:
    print("NO")
