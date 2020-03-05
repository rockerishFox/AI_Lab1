def test4():
    string = ""

    assert (solve4(string) == "")
    string = "a"
    assert (solve4(string) == "a ")
    string = " a a a a a "
    assert (solve4(string) == "")
    string = "a b c d "
    assert (solve4(string) == "a b c d ")
    string = "a a b b a c d e"
    assert (solve4(string) == "c d e ")



    print("Teste problema 4 - done!")


def solve4(text):
    contor = []
    for word in text.split():
        found = 0
        for el in contor:
            if el[0] == word:
                el[1] += 1
                found = 1
                break
        if not found:
            contor.append([word, 1])

    final = ""
    for el in contor:
        if el[1] == 1:
            final += el[0] + " "
    return final


def main():
    test4()


main()