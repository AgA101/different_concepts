class Account:
    amount: int
    def __init__(self,amount: int):
        self.amount = amount

def fun(a : int,b : int) -> None:
    return a * b


a  : int = 6
print(fun(3,5.3))
mike = Account(160.9)

from typing import List, Tuple, Dict, Union, Optional

number = Union[int,float]

def fun(a : number,b : number) -> number:
    return a * b

numbers: List[int] = [4, 6, 7]
numbers.append('8')
data: Tuple[str,int] = ('Nick', 23)
g: Dict[str, int] = {'a': 5, 'b': 7, 'c': 5, 'd': 3}
print(fun(3,4))
