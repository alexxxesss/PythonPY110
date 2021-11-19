if __name__ == "__main__":
    stroka = 'asdfwnkdfngdkfmn234g'

    list_elem = [x for x in stroka]
    list_numb = [i for i in range(len(stroka))]

    # print(list(zip(list_numb, list_elem)))
    for z in zip(list_numb, list_elem):
        print(z)
