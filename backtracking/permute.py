# [not written by me]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Yield all permutations of `seq` (any iterable) iteratively,
        in lexicographic order.

        Follows the classic “next-permutation” algorithm (sometimes called Narayana’s algorithm and described in Knuth Vol. 4A §7.2.1.2).

        """
        perms = []
        a = sorted(nums)  # start with the smallest permutation
        n = len(a)
        perms.append(a.copy())

        while True:
            # 1. find right-most ascent: largest i with a[i] < a[i+1]
            for i in range(n - 2, -1, -1):
                if a[i] < a[i + 1]:
                    break
            else:  # already at the last permutation
                return perms

            # 2. find element just larger than a[i] to the right of i
            for j in range(n - 1, i, -1):
                if a[j] > a[i]:
                    break

            # 3. swap them …
            a[i], a[j] = a[j], a[i]

            # 4. … and reverse the suffix a[i+1:]
            a[i + 1:] = reversed(a[i + 1:])

            perms.append(a.copy())


nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))
