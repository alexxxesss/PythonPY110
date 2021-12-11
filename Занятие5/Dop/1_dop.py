# Скрипт для конвертации списка с 1 и 0, в целочисленное значение.
# Списки могут иметь разную длину.

def some_func(n):
    return int(''.join(map(str, n)), 2)


if __name__ == "__main__":

    bin_list = [0, 1, 1, 0]
    print(some_func(bin_list))
