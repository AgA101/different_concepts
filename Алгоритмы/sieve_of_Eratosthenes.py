n = int(input())
a = [i % 2 for i in range(n + 1)]
a[2] = True
k = 3
while k * k <= n:
    if a[k]:
        i = k * k
        while i <= n:
            a[i] = False
            i += 2 * k
    k += 1

p = [i for i in range(2, n+1) if a[i]]
print(*p)