def func_reg(list_: list) -> list:
    return list(map(lambda x: " ".join(x), list_))


if __name__ == "__main__":

    list_of_tuples = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

    print(func_reg(list_of_tuples))
