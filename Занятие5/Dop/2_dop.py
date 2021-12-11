# Скрипт имитирующий зрительскую волну для строки.
# Строка ввода всегда будет в нижнем регистре, но может быть пустой.
# Если символ в строке является пробелом, пропустите его.

def upp(st):
    for i in range(len(st)):
        if not st[i] == " ":
            up_w = st[i].upper()
            print(f'{st[:i]}{up_w}{st[i+1:]}')


if __name__ == "__main__":

    stroka = 'hello world'
    upp(stroka)
