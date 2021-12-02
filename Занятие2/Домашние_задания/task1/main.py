def func_geom(q: int, num: int):
    n = 1
    while True:
        yield num * (q ** (n - 1))
        n += 1


if __name__ == "__main__":
    denominator = int(input('Введите знаменатель геометрической прогрессии: '))
    first_num = int(input('Введите первый член прогрессии: '))
    count = int(input('Введите сколько чисел последовательности нужно вывести на экран: '))

    geometric_progression = func_geom(denominator, first_num)

    for _ in range(count):
        print(next(geometric_progression))
