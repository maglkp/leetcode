# [not written by me]
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Yield all length-k combinations chosen from 1..n, generated
        iteratively (no recursion)

        Follows the lexicographic algorithm described by Knuth (vol. 4A, §7.2.1.3).

        """
        combinations = []
        if k < 0 or k > n:
            return []
        combo = list(range(1, k + 1))  # start with [1, 2, …, k]
        limit = [n - k + i + 1 for i in range(k)]  # [n-k+1, …, n]

        while True:
            combinations.append(combo.copy())  # visit current combination

            # find the rightmost element that can be incremented
            for i in reversed(range(k)):
                if combo[i] != limit[i]:
                    break
            else:  # all elements at their limits
                return combinations

            combo[i] += 1  # bump that element
            # reset the tail to the minimal lexicographic values
            for j in range(i + 1, k):
                combo[j] = combo[j - 1] + 1
