from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return ""

    max_common_sublen = len(strs[0])
    for s in strs:
        if len(s) < max_common_sublen:
            max_common_sublen = len(s)

    longest_prefix = 0
    for i in range(max_common_sublen):
        if not all_equal(strs, i):
            break
        longest_prefix += 1

    return strs[0][0:longest_prefix]


def all_equal(strs: List[str], i: int):
    v = strs[0][i]
    for s in strs:
        if s[i] != v:
            return False
    return True
