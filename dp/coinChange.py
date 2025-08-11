from typing import List, Set


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        v = self.coin_change_dp(coins, amount, {})
        return -1 if v == float('inf') else v

    def coin_change_dp(self, coins: List[int], amount: int, memo: dict) -> int:
        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        current = float('inf')
        for coin in coins:
            rest = amount - coin
            if rest < 0:
                continue
            current = min(current, self.coin_change_dp(coins, rest, memo))
            # memo[rest] = current

        memo[amount] = current + 1
        return current + 1


coins = [1, 2, 5]
amount = 11
coins = [2]
amount = 3
s = Solution()
print(s.coinChange(coins, amount))
