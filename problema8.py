from queue import Queue


def test8():
    n = 1
    assert (solve8(n) == ["1"])
    n = 0
    assert (solve8(n) == [])
    n = 4
    assert (solve8(n) == ["1","10","11","100"])
    n = 5
    assert (solve8(n) == ["1","10","11","100","101"])
    n = -5
    assert (solve8(n) == [])

    print("Teste problema 8 - doen!")


def solve8(n):
    q = Queue()
    result = []
    q.put("1")
    while (n > 0):
        n -= 1

        s1 = q.get()
        result.append(s1)

        s2 = s1
        q.put(s1 + "0")
        q.put(s2 + "1")
    return result

def main():
    test8()

main()