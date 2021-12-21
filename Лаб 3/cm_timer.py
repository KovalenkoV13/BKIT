import time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('time: {}'.format(time.time() - self.start))


@contextmanager
def cm_timer_2():
    cur = time.time()
    yield cur
    print('time: {}'.format(time.time() - cur))


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)