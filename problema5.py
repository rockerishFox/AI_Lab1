def test5():
    list = [1,2,3,4,5,2]
    assert (solve5(list) == 2)
    list = []
    assert (solve5(list) == 0)
    list = [2,1,4,2,3]
    assert (solve5(list) == 2)
    list = [1,1,2,3]
    assert (solve5(list) == 1)

    print("Teste problema 5 - done!")


def solve5(list):
    contor = [0] * len(list)
    for el in list:
        if contor[el - 1] == 0:
            contor[el - 1] = 1
        else:
            return el
    return 0


def main():
    test5()

main()