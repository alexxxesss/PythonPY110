# Найти слово в строке с наивысшей оценкой.
# Оценку слов проводить по буквам (символы не оцениваются), в соответсвии с
# позицией в алфавите (регистр можно не учитывать):
# example
# а=1, б=2, в=3 и т.д.

def valuation(st):
    new_st = st.lower().split()
    list_value = []
    for i in new_st:
        value = 0
        for x in i:
            if x.isalpha():
                value += ord(x)
        list_value.append(value)
    return print(st.split()[max(list(enumerate(list_value, 0)), key=lambda num:num[1])[0]])



if __name__ == "__main__":

    stroka = 'Добрый день Господин'
    valuation(stroka)
