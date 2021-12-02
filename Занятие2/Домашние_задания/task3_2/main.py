if __name__ == "__main__":
    def check_int(fn):
        def wrapper(*args):
            for i in args:
                if not isinstance(i, int):
                    raise TypeError(f"Передаваемые аргументы не числа!")
            result = fn(*args)
            return result
        return wrapper

    @check_int
    def some_func(*args):
        summ = sum(args)
        print(summ)

    some_func(1, 2, 5)
