from typing import Generator

def Fibonacci(value: int) -> Generator:
    a0: int = 0
    a1: int = 1
    k: int = 1
    while k <= value:

        k += 1
        a0, a1 = a1, a0 + a1
    yield a0

for item in Fibonacci(int(input())):
    print(item)