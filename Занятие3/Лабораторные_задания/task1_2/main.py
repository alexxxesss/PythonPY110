OUTPUT_FILE = "output.txt"


def task(steps=11):
    with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:  # TODO записать лесенку в файл
        for i in range(1, steps):
            line = '*' * i
            f.write(line.rjust(steps - 1))
            f.write("\n")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
