# find number of 2s and 5s in all factors of n! (2,5 = 10s factors) and min(2s, 5s) is the number of times we can divide by 10
# optimization - only find 5s as it'll always be less or equal of them

class Solution:
    def trailingZeroes(self, n: int) -> int:

        fives = 0
        for i in range(1, n + 1):
            num = i
            while num % 5 == 0:
                num /= 5
                fives += 1

        return fives
