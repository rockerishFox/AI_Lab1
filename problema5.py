def test5():
    list = [1, 2, 3, 4, 5, 2]
    assert (solve5(list) == 2)
    list = []
    assert (solve5(list) == 0)
    list = [2, 1, 4, 2, 3]
    assert (solve5(list) == 2)
    list = [1, 1, 2, 3]
    assert (solve5(list) == 1)

    list = [1, 2, 3, 4, 5, 2]
    assert (solve5var2(list) == 2)
    list = []
    assert (solve5var2(list) == 0)
    list = [2, 1, 4, 2, 3]
    assert (solve5var2(list) == 2)
    list = [1, 1, 2, 3]
    assert (solve5var2(list) == 1)

    print("Teste problema 5 - done!")


def solve5(list):
    contor = [0] * len(list)
    for el in list:
        if contor[el - 1] == 0:
            contor[el - 1] = 1
        else:
            return el
    return 0


def solve5var2(list):
    sortedlist = sorted(list)
    if len(list) == 0:
        return 0
    el = list[0]
    for i in range(1, len(list)):
        if el == sortedlist[i]:
            return el
        el = sortedlist[i]
    return 0


def main():
    test5()


main()
