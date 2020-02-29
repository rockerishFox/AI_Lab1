def tests10():
    matrix = [
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1]
    ]

    assert (solve10(matrix) == 3)

    matrix = []

    assert (solve10(matrix) == 0)

    matrix = [
        [1, 1],
        [0, 1],
        [0, 0]
    ]

    assert (solve10(matrix) == 1)

    matrix = [
        [1, 1],
        [1, 1],
        [1, 1]
    ]

    assert (solve10(matrix) == 1)

    print("Teste problema 10 - done!")


def solve10(matrix):
    max = 0
    line = -1
    for j in range(len(matrix)):
        ones = 0
        row = matrix[j]
        for i in range(len(row)):
            if row[i] != 0:
                ones = len(row) - i
                break
        if ones > max:
            max = ones
            line = j

    return line + 1


def menu():
    tests10()


menu()
