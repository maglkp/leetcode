from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        buy_ix = self.find_last_non_increasing(prices, 0)
        sell_ix = self.find_last_non_decreasing(prices, buy_ix + 1)

        while buy_ix != sell_ix and sell_ix < len(prices) and buy_ix < len(prices):
            max_profit += prices[sell_ix] - prices[buy_ix]
            buy_ix = self.find_last_non_increasing(prices, sell_ix + 1)
            sell_ix = self.find_last_non_decreasing(prices, buy_ix + 1)

        return max_profit

    def find_last_non_increasing(self, prices: List[int], start_ix: int) -> int:
        ix = start_ix
        while ix < len(prices) - 1 and prices[ix] >= prices[ix + 1]:
            ix += 1

        return ix

    def find_last_non_decreasing(self, prices: List[int], start_ix: int) -> int:
        ix = start_ix
        while ix < len(prices) - 1 and prices[ix] <= prices[ix + 1]:
            ix += 1

        return ix


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(prices))
