def mod_checker(x, mod=0):
    return lambda y: True if y / x == mod


if __name__ == "__main__":

    mod_3 = mod_checker(3)
    print(mod_3(3))
    print(mod_3(4))
    mod_3_1 = mod_checker(3, 1)
    print(mod_3_1(4))