from  typing import Any, Generator

def repeater(value: Any) -> Generator:
    while True:
        value += 1
        yield value

for item in repeater(5):
    print(item)