from functools import wraps
import time


def process_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = round(time.time() * 1000)
        result = func(*args, **kwargs)
        end = round(time.time() * 1000)
        total = end - start
        return result, total
    return wrapper


@process_timer
def sleep_test():
    time.sleep(1)
    return True


@process_timer
def list_sort(unsorted):
    unsorted.sort()

    return unsorted


if __name__ == "__main__":
    sleep_timer = sleep_test()
    print(sleep_timer)
    assert sleep_timer[0] is True and sleep_timer[1] > 999
