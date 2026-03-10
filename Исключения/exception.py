def divide(a,b):
    return a / b

try:
    x, y = [int(x) for x in input().split()]
    res = divide(x,y)
    print(res)
except ZeroDivisionError:
    print("Делить на ноль нельзя")
except ValueError as error:
    print(error)

