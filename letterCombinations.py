# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import Dict
from typing import List


def letterCombinations(self, digits: str) -> List[str]:
    maps = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    # digits = list(digits)
    # digits.sort()
    # for ix, d in digits:

    results = []
    gen("", results, [], digits, maps)

    return results


def gen(self, results: List[str], acc: List[str], digits: str, maps: Dict[str, List[str]]):
    # digits = "23"
    # results = ["ad","ae","af"...
    # acc =

    # recursive
    # f (results, acc, digits)
    # if digits empty add acc to list and return
    if len(digits) == 0:
        if len(acc) > 0:
            results.append("".join(acc))
        return

    # take first digit, iterate through
    for letter in maps[digits[0]]:
        gen("", results, acc + [letter], digits[1:], maps)


#print(letterCombinations("", "23"))
print(letterCombinations("", ""))
