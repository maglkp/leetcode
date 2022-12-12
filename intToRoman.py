def intToRoman(num: int) -> int:
    letters = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }
    letterValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    letterThresholds = {
        'I': 0.9,
        'V': 0.8,
        'X': 0.9,
        'L': 0.8,
        'C': 0.9,
        'D': 0.8,
        'M': 0.9
    }
    shorteners = {
        'M': 'C',
        'D': 'C',
        'C': 'X',
        'L': 'X',
        'X': 'I',
        'V': 'I'
    }

    v = ''
    for item in letters.items():
        letterValue = item[0]
        letter = item[1]

        curLettersCount = num / letterValue
        whole = int(curLettersCount)
        for _ in range(whole):
            v += letters[letterValue]
            num -= letterValue
        #if (curLettersCount - whole) >= letterThresholds[letter]:
        if (curLettersCount - float(whole)) > letterThresholds[letter] - 0.001:
            shortener = shorteners[letter]
            v += shortener + letter
            num -= letterValue - letterValues[shortener]
    #print(v)
    return v


def test(expected, n):
    if intToRoman(n) == expected:
        print(".")
    else:
        print("failed " + str(n))


test("I", 1)
test("II", 2)
test("III", 3)
test("IV", 4)
test("VI", 6)
test("XVI", 16)
test("XIX", 19)
test("XLIV", 44)
test("LVIII", 58)
test("MM", 2000)
test("MCMXCIV", 1994)
test("MMMLVIII", 3058)
