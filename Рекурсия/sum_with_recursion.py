def recursion_sum():
    a = int(input())
    if a != 0: 
        return a + recursion_sum()
    return 0
    
print(recursion_sum())


