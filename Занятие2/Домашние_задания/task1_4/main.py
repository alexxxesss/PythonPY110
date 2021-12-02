def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]


def task():
    for pair in pairwise("ABCDEFG"):
        print(pair[0] + pair[1])


if __name__ == "__main__":
    task()
