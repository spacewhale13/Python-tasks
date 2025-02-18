numbers = [8, 9, 10, 11]
numbers[1] = 17

"""for i in range(4, 7):
    numbers.append(i)"""
numbers.extend([4, 5, 6])
del numbers[0]

numbers.extend(numbers)

numbers.insert(3, 25)
print(numbers)
