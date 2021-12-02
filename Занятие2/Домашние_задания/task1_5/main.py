import random
from string import ascii_lowercase, ascii_uppercase, digits


def func_gen(k):
    all_word = ascii_lowercase + digits + ascii_uppercase
    yield ''.join(random.sample(all_word, k))


if __name__ == "__main__":
    # print(ascii_lowercase)
    # print(ascii_uppercase)
    # print(digits)
    k = int(input('Введите количество символов, из которых будет состоять пароль: '))
    gen_password = func_gen(k)
    print(next(gen_password))
