class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsRec(n, {})

    def climbStairsRec(self, n: int, memo: dict) -> int:
        if n in memo:
            return memo[n]
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        n1 = self.climbStairsRec(n - 1, memo)
        n2 = self.climbStairsRec(n - 2, memo)
        memo[n] = n1 + n2
        return n1 + n2


s = Solution()
for _ in range(10):
    print(s.climbStairs(_))
#print(s.climbStairs(10))