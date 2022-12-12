def romanToInt(s: str) -> int:
    letters = {
        '': 0,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    v = 0
    last = 0
    for c in s:
        current = letters[c]
        v += current
        if last < current:
            v -= 2 * last
        last = current
    return v


def test(s, expected):
    if romanToInt(s) == expected:
        print(".")
    else:
        print("failed " + s)


test("I", 1)
test("II", 2)
test("III", 3)
test("IV", 4)
test("VI", 6)
test("XVI", 16)
test("MCMXCIV", 1994)
test("MMMLVIII", 3058)
test("XLIV", 44)
