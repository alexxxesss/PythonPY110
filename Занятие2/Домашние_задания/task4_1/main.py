if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    def pairwise(points):
        for i in range(len(points) - 1):
            yield (((points[i+1][0] - points[i][0]) ** 2) + ((points[i+1][1] - points[i][1]) ** 2)) ** 0.5

    def func():
        summa = 0
        for length in pairwise(pts):
            summa += length
        return summa

    print(func())
