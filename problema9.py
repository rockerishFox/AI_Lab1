def tests9():
    matrix = [[1, 2, 2, 1, 4],
              [4, 4, 5, 2, 1],
              [1, 2, 2, 4, 5]
              ]
    c1 = (0, 0)
    c2 = (1, 1)
    assert (solve9(matrix, c1, c2) == 11)

    c1 = (1, 1)
    c2 = (0, 0)
    assert (solve9(matrix, c1, c2) == 11)

    try:
        c1 = (-1, 1)
        c2 = (0, 5)
        solve9(matrix, c1, c2)
        assert False
    except ValueError:
        assert True

    try:
        c1 = (0, 0)
        c2 = (0, 6)
        solve9(matrix, c1, c2)
        assert False
    except ValueError:
        assert True

    print("Teste problema 9 - done!")


def coordinatesOverZero(c1, c2):
    if c1[0] < 0 or c2[0] < 0:
        return False
    if c1[1] < 0 or c2[1] < 0:
        return False
    return True


def coordinatesInRange(c1, c2, n):
    if c1[0] > len(n[0]) or c2[0] > len(n[0]):
        return False
    if c1[1] > len(n) or c2[1] > len(n):
        return False
    return True


def solve9(matrix, coord1, coord2):
    if coord2 < coord1:
        aux = coord1
        coord1 = coord2
        coord2 = aux

    sum = 0

    if not coordinatesOverZero(coord1, coord2):
        raise ValueError("Nu putem avea coordonate negative!")

    if not coordinatesInRange(coord1, coord2, matrix):
        raise ValueError("Coordonate depasesc lungimea matricei!")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if coord1[0] <= i <= coord2[0] and coord1[1] <= j <= coord2[1]:
                sum += matrix[i][j]

    return sum


def main():
    tests9()


main()
