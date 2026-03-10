from random import randint
num = [randint(-50,50) for x in range(10)]

num.sort(key=lambda x: x ** 2)

print(*num)
print(*filter(lambda x : x >= 10, num))
