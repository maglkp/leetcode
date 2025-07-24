class Solution:
    def reverseBits(self, n: int) -> int:

        output = 0
        for _ in range(32):
            bit = n & 1
            output <<= 1
            output |= bit
            n >>= 1

        return output



s = Solution()
print(s.reverseBits(6))
print(s.reverseBits(43261596))
