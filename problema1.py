def test1():
    string = ""

    assert (solve1(string) == "")
    string = "avem mre"
    assert (solve1(string) == "mre")

    string = "Avem avem"
    assert (solve1(string) == "Avem")

    string = "sigur se stie"
    assert (solve1(string) == "stie")

    string = "stiii stiiiii"
    assert (solve1(string) == "stiiiii")

    print("Teste problema 1 - done!")


def solve1(text):
    last = ""
    for word in text.split():
        if word.lower() > last.lower():
            last = word
    return last


def main():
    test1()

main()