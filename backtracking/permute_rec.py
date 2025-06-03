from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        solutions = []
        self.permute_rec(solutions, nums, [], len(nums))
        return solutions

    def permute_rec(self, solutions, items, acc, k):
        if len(acc) == k:
            solutions.append(acc)
            return

        for i in range(len(items)):
            self.permute_rec(solutions, items[:i] + items[i + 1:], acc + [items[i]], k)


nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))
