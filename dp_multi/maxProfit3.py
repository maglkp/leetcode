from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = [0] * len(prices)
        buy = 0
        # sell = 0
        # max_profit = int("-inf")
        for ix in range(1, len(prices)):
            left[ix] = max(left[ix - 1], prices[ix] - prices[buy])
            if prices[ix] < prices[buy]:
                buy = ix

        right = [0] * len(prices)
        sell = len(prices) - 1
        for ix in range(len(prices) - 2, -1, -1):
            right[ix] = max(right[ix + 1], prices[sell] - prices[ix])
            if prices[ix] > prices[sell]:
                sell = ix

        max_profit = 0
        for ix in range(len(prices)):
            max_profit = max(max_profit, left[ix] + right[ix])

        return max_profit


s = Solution()
print(s.maxProfit([1, 2, 3, 7, 2, 0, 2, 8]))
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
