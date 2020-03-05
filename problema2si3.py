from math import sqrt


def testsProblema3():
    v1 = [1, 0, 2, 0, 3]
    v2 = [1, 2, 0, 3, 1]
    assert (solve3(v1, v2) == 4)

    v1 = [0, 0, 2]
    v2 = [1, 2, 2, 3, 1]
    assert (solve3(v1, v2) == 4)

    v1 = [6, 0, 2, 0, 3]
    v2 = [6, 2, 0, 3]
    assert (solve3(v1, v2) == 36)

    v1 = [0, 0, 2, 0, 3]
    v2 = [0, 2, 0, 3, 0]
    assert (solve3(v1, v2) == 0)

    v1 = [1, 1, 2, 1, 3]
    v2 = [1, 2, 1, 3, 1]
    assert (solve3(v1, v2) == 11)

    v1 = []
    v2 = []
    assert (solve3(v1, v2) == 0)

    print("Teste problema 3 - done!")


def testsProblema2():
    p1 = (1, 5)
    p2 = (4, 1)
    assert (solve2(p1, p2) == 5.0)

    p1 = (2, 4)
    p2 = (26, 9)
    assert (solve2(p1, p2) == 24.52)

    p1 = (5, 3)
    p2 = (14, 3)
    assert (solve2(p1, p2) == 9.0)

    p1 = (9, 7)
    p2 = (14, 3)
    assert (solve2(p1, p2) == 6.40)

    p1 = (0, 0)
    p2 = (0, 0)
    assert (solve2(p1, p2) == 0)

    print("Teste problema 2 - done!")


def solve2(pair1, pair2):
    sum1 = pair2[0] - pair1[0]
    sum2 = pair2[1] - pair1[1]
    return round(sqrt(sum1 * sum1 + sum2 * sum2), 2)


def solve3(vector1, vector2):
    min = len(vector1)

    if len(vector2) < len(vector1):
        min = len(vector2)

    sum = 0

    for i in range(min):
        sum += vector1[i] * vector2[i]

    return sum


def main():
    testsProblema2()
    testsProblema3()
    print(solve3([1, 2, 3, 0], [2, 0, 0, 0]))
    print(solve2((2, 4), (26, 9)))


main()