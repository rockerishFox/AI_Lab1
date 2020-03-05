def test6():
    list = [1, 2, 3, 2, 2, 3, 2, 2]
    assert (solve6(list) == 2)
    list = [1, 1, 3, 2, 2, 3, 2, 2]
    assert (solve6(list) == 0)
    list = [1, 1, 1, 1, 2, 2, 2, 2]
    assert (solve6(list) == 0)
    list = [1, 1, 3, 2, 2]
    assert (solve6(list) == 0)
    list = []
    assert (solve6(list) == 0)
    print("Teste problema 6 - done!")


def solve6(list):
    if len(list) == 0:
        return 0

    max = [0, 0]
    sortedlist = sorted(list)
    contor = 1
    ex = sortedlist[0]
    for i in range(1, len(sortedlist)):
        if sortedlist[i] == ex:
            contor += 1
        else:
            if contor > max[1]:
                max[1] = contor
                max[0] = ex
            contor = 1
        ex = sortedlist[i]

    if max[1] > len(list) // 2:
        return max[0]
    return 0


def main():
    test6()


main()
