def product(a,*args):
    for i in range(len(args)):
        a *= args[i]
    return a
print(product(3,5,8))