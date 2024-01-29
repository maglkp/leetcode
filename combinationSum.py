# 25 min
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.generate(results, [], candidates, target)
        return results

    def generate(self, results: List[List[int]], acc: List[int], candidates: List[int], target: int) -> None:
        if sum(acc) == target:
            results.append(acc)
            return

        for c_ix in range(len(candidates)):
            if sum(acc) + candidates[c_ix] <= target:
                self.generate(results, acc + [candidates[c_ix]], candidates[c_ix:], target)


s = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(s.combinationSum(candidates, target))
