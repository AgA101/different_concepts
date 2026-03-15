b = int(input())
s = ''
while b != 0:
    s += str(b % 2)
    b = b // 2
print(s[::-1])
