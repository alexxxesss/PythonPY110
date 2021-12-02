def min_len_check(fn):
    def wrapper(arg):
        if len(arg) < 10:
            raise ValueError("Строка слишком короткая")

        print('С этой строкой все хорошо')
        print("=" * 25)
        result = fn(arg)
        return result

    return wrapper


@ min_len_check
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
