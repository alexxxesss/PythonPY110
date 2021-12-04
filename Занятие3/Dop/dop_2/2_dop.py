# Написать генератор, возвращающий по 3 символа из текстового файла, при этом не загружая в память весь файл.

INPUT_FILE = 'input.txt'


def gen_func(n):
    with open(INPUT_FILE, 'r') as f:
        for _ in range(n):
            yield f.read(n)


return_3 = gen_func(4)

if __name__ == "__main__":

    print(next(return_3))
    print("some text")
    print(next(return_3))
