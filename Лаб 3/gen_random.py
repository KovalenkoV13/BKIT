import random


def gen_random(num_count, begin, end):
    cur = 0 #текущее значение
    while cur < num_count:
        cur += 1
        yield random.randint(begin, end)
