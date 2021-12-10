# Написать генератор, возвращающий по одной строке из текстового файла. Символом окончания строки является символ “\n”. Встроенной реализацией пользоваться нельзя.
INPUT_FILE = 'input.txt'


def gen_func():
    with open(INPUT_FILE, 'r', encoding="utf-8") as f:
        for i in f.read().split('\n'):
            yield i


return_string = gen_func()


if __name__ == "__main__":

    print(next(return_string))
    print("some text")
    print(next(return_string))
    print(next(return_string))
    print(next(return_string))
    print(next(return_string))
    print("some text")
    print(next(return_string))
    print(next(return_string))
