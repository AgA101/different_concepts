def prime_factorization(n):
    d = 2
    ans = []
    while d * d <= n:
        while n % d == 0:
            n //= d
            ans.append(d)
        d += 1
    if n > 1:
        ans.append(n)
    return ans

print(prime_factorization(int(input())))