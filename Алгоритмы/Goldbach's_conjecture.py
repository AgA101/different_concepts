def P(n):
    d = 2
    while d * d <= n and n % d > 0:
        d += 1
    return d * d > n
n = int(input())
w = 2
while not(P(w) and P(n - w)):
    w += 1
print(w, n - w, sep = " ")