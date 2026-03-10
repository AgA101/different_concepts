from typing import Generator

def gen_powers_of_two(max_pow: int) -> Generator:
    cur_pow: int = 0
    while 2 ** cur_pow < max_pow:
        yield 2 ** cur_pow
        cur_pow += 1

for item in gen_powers_of_two(int(input())):
    print(item)