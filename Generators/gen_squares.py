from typing import Generator

def gen_squares(max_pow: int) -> Generator:
    cur_pow: int = 0
    while cur_pow * cur_pow <= max_pow:
        yield cur_pow * cur_pow
        cur_pow += 1

for item in gen_squares(int(input())):
    print(item)