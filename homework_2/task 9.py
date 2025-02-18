s = input().split(" ")
pair = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            pair += 1
print(pair)
