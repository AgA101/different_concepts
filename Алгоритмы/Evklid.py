def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
        
a1, b1 = map(int,input().split())
print(GCD(a1,b1))
