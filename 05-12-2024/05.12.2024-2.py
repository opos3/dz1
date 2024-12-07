import time

def timer_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Функція '{func.__name__}' виконалася за {elapsed_time:.6f} секунд.")
        return result
    return wrapper


@timer_decorator
def example_function(n):

    total = 0
    for i in range(n):
        total += i ** 2
    return total


@timer_decorator
def test_fast_function():
    return sum(range(10))

@timer_decorator
def test_slow_function():
    time.sleep(1)
    return "done"


if __name__ == "__main__":
    print("Результат example_function:", example_function(100000))
    print("Результат test_fast_function:", test_fast_function())
    print("Результат test_slow_function:", test_slow_function())