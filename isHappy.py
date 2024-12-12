class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = self.sumOfSquaredDigits(str(n))


    def sumOfSquaredDigits(self, num: str):
        total = 0
        for c in num:
            total += int(c) ** 2
        return total

n = 2
s = Solution()
print(s.isHappy(n))