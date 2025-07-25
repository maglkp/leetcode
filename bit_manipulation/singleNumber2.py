from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32

        # search in non-negative numbers first only
        for num in nums:
            if num >= 0:
                ix = 0
                v = num
                for _ in range(32):
                    bits[ix] += v & 1
                    ix += 1
                    v >>= 1

        r = reversed(bits)
        no3s = [str(e % 3) for e in r]
        candidate = int("".join(no3s), 2)

        if candidate in nums:
            return candidate

        # search in negative numbers only
        for num in nums:
            if num < 0:
                ix = 0
                v = -num
                for _ in range(32):
                    bits[ix] += v & 1
                    ix += 1
                    v >>= 1

        r = reversed(bits)
        no3s = [str(e % 3) for e in r]
        candidate = int("".join(no3s), 2)

        return -candidate



s = Solution()
a = [2, 2, 3, 2]
a = [30000, 500, 100, 30000, 100, 30000, 100]
a = [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
print(s.singleNumber(a))
