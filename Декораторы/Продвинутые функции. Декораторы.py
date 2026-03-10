def fun(a,b,c,d,*args,**kwargs):
    print(args)
    #print(len(args))
    print(kwargs)
    return a , b , c , d


print(fun(3,7,5,6,8))
#print(fun((3,7,5,67,e=7,f=0))
#print(fun(a=7, b=3, c=0))
data = (2,7,8,3)
print(fun(*data))
g = {'a' : 5, 'b' : 7,'c': 5,'d':3}
print(fun(**g))