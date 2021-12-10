# Написать генератор, возвращающий по одному слову текстового файла, при этом не загружая в память весь файл. В качестве разделителя слов использовать символ пробела.

INPUT_FILE = 'input.txt'


def gen_func():
    with open(INPUT_FILE, 'r', encoding="utf-8") as f:
        for i in str.split(f.read()):
            yield i


return_word = gen_func()


if __name__ == "__main__":

    print(next(return_word))
    print("some text")
    print(next(return_word))
    print(next(return_word))
    print(next(return_word))
    print(next(return_word))
    print("some text")
