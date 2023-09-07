# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target
# uses list backed hash map to find all elements that match the remainder that's needed to complete the sum
from typing import List


def numOfPairs(self, nums: List[str], target: str) -> int:
    num_to_ix = {}
    for ix, v in enumerate(nums):
        if num_to_ix.get(v) is None:
            num_to_ix[v] = [ix]
        else:
            num_to_ix[v].append(ix)

    n = 0
    for ix, num in enumerate(nums):
        noprefix = target.removeprefix(num)
        ix_list = num_to_ix.get(noprefix)

        if ix_list is not None:
            n += len(list(filter(lambda v: v != ix, ix_list)))
    return n


# print(numOfPairs("", ["777","7","77", "77"], "7777"))
print(numOfPairs("", ["1", "1", "1"], "11"))
