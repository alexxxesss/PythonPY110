def func_reg(words: list):
    new_list_upper = list(dict.fromkeys(map(str.upper, words)))
    new_list_lower = list(dict.fromkeys(map(str.lower, words)))
    return list(zip(new_list_upper, new_list_lower))


if __name__ == "__main__":
    input_list = [
        "U",
        "f",
        "a",
        "b",
        "i",
        "o",
        "E",
        "B",
        "A"
    ]

    print(func_reg(input_list))
