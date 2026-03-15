def factor(n):
    d = 2
    ans = n
    while d * d <= n and ans == n:
        while n % d == 0:
            n //= d
            ans = d
        d += 1
    return ans
print(factor(int(input())))