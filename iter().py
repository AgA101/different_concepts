num = [5, 6, 0]

iterator = iter(num)


while True:
    try:
        a = next(iterator)
        print(a)
    except StopIteration:
        break
#print(iterator)
#for item in num:
 #   print(item)
