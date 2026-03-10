def corountine():
    while True:
        value = (yield)
        print(value)
routine = corountine()
next(routine)
routine.send(5)
routine.send(True)
routine.close()