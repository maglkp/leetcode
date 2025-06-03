from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

            items = list(range(1, n + 1))
            solutions = []
            self.combine_rec(solutions, items, [], k)
            return solutions

    def combine_rec(self, solutions, items, acc, k):
        if len(acc) == k:
            solutions.append(acc)
            return

        for i in range(len(items)):
            self.combine_rec(solutions, items[i + 1:], acc + [items[i]], k)