def digit_count(number, base):
    count = 0
    while number > 0:
        count += 1
        number //= base
    return count


def is_polindrom(number, base):
    count = digit_count(number, base)
    highest_place = base ** (count - 1)
    for _ in range(count // 2):
        if number % base != number // highest_place:
            return False
        number %= highest_place
        number //= base
        highest_place //= base * base
    return True
    
print(is_polindrom(102,10))