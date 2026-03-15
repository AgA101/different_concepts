def prime_factorization_pow(n):
    ans = []
    d = 2
    while d * d <= n:
        count = 0
        while n % d == 0:
            n //= d
            count += 1
        if count > 0:
            ans.append([d, count])
        d += 1
    if n > 1:
        ans.append([n, 1])
    return ans

n = int(input())
print(prime_factorization_pow(n))

