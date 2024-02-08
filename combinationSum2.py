# 30 mins
# time limit exceeded computing duplicate results
from typing import List, Set


class Solution:

    def __init__(self):
        self.ct = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates_counts = [0 for _ in range(50)]
        for c in candidates:
            if c * candidates_counts[c-1] < target:
                candidates_counts[c-1] += 1

        # transform counts back to list
        candidates = []
        for i in range(50):
            if candidates_counts[i] > 0:
                candidates.extend([i+1] * candidates_counts[i])

        results = set()
        if sum(candidates) >= target:
            self.generate(results, [], candidates, target)

        return list(results)

    def generate(self, results: Set[tuple[int]], acc: List[int], candidates: List[int], target: int) -> None:
        self.ct += 1
        if sum(acc) == target:
            results.add(tuple(sorted(acc)))
            return

        len_c = len(candidates)
        for c_ix in range(len_c):
            if sum(acc) + candidates[c_ix] <= target:
                self.generate(results, acc + [candidates[c_ix]], candidates[c_ix + 1:], target)


s = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
target = 30

candidates = [1, 1, 1, 1, 1]
target = 5
candidates = [1, 2, 3, 4, 5]
target = 15
sum_ = s.combinationSum2(candidates, target)
print(sum_)
