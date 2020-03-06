def test7():

    list = [7,4,5,6,3,9]
    k=2
    assert (solve7(list,k) == 7)

    list = [7,7,7]
    k=2
    assert (solve7(list,k) == 7)

    list = []
    k=2
    assert (solve7(list,k) == 0)

    list = [7]
    k=2
    assert (solve7(list,k) == 0)

    list = [1,2,3,4,7]
    k=4
    assert (solve7(list,k) == 2)


    print("teste problema 7 - done!")


def solve7(list, k):
    if k not in range(len(list)):
        return 0

    sortedList = sorted(list, reverse=True)
    return sortedList[k-1]

def main():
    test7()


main()
