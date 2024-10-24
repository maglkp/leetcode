from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min_val = gas[0] - cost[0]
        min_ix = 0
        acc = 0
        for i in range(len(gas)):
            gas[i] -= cost[i]
            acc += gas[i]
            if acc < min_val:
                min_ix = i
                min_val = acc

        candidate_ix = (min_ix + 1) % len(gas)
        acc = 0
        for i in range(len(gas)):
            ix = (candidate_ix + i) % len(gas)
            acc += gas[ix]
            if acc < 0:
                return -1

        return candidate_ix


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
gas = [2, 3, 4]
cost = [3, 4, 3]
s = Solution()
print(s.canCompleteCircuit(gas, cost))
