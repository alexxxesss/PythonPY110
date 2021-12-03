def func_reg(dict_: dict):
    output_list = list(map(lambda x: {'Наука': x[0], 'Язык': x[1]}, zip(*dict_.values())))
    return output_list


if __name__ == "__main__":

    input_dict = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}

    print(func_reg(input_dict))
