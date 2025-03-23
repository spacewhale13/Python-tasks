m = int(input())
p = int(input())
n = int(input())
for i in range(1, n + 1):
    res = m * (1 + p / 100) ** i
    print(i, res)
