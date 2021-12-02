import random
import time


def time_decorator(fn):
    print("Этот код будет выведен в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")

        start = time.time()
        result = fn(*args, **kwargs)
        time.sleep(random.randint(0, 5))
        print(time.time() - start)

        print("Этот код будет выполняться после каждого вызова функции")
        return result
    return wrapper


@time_decorator
def pow_(a, n):
    return pow(a, n)

pow_with_decorator = time_decorator(pow_)

if __name__ == "__main__":
    print(pow_)
    print("=" * 25)

    print(pow_(5, 2))
    print("=" * 25)

    print(pow_(4, 4))

    pow_with_decorator(5, 2)