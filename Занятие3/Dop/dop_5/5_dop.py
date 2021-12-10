# Написать генератор, возвращающий  последние n строк из текстового файла, при этом не загружая в память весь файл.
INPUT_FILE = 'input.txt'


def gen_func(n):
    with open(INPUT_FILE, 'r', encoding="utf-8") as f:
        yield ''.join(f.readlines()[-n:])


return_last_string = gen_func(5)


if __name__ == "__main__":

    print(next(return_last_string))
