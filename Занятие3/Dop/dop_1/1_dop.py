# Написать декоратор, сохраняющий результат в файл output.txt помимо возвращения. Результаты должны накапливаться в файле.

OUTPUT_FILE = 'output.txt'

def decorator(fn):
    def wrapper(*args):
        result = fn(*args)
        with open(OUTPUT_FILE, 'a', encoding="utf-8") as f:
            for i in result:
                f.write(str(i) + "\n")
        return result
    return wrapper


@decorator
def some_func(*args):
    return args


if __name__ == "__main__":

    print(some_func(1, 2, 3, 4))
    print(some_func('Hello', 'Привет'))
    print(some_func("World"))
