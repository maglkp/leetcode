class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x

        while left < right:
            mid = (left + right) // 2

            mm = mid * mid
            if mm <= x < (mid + 1) * (mid + 1):
                 return mid

            if mm < x:
                left = mid + 1
            else:
                right = mid - 1

        return left



s = Solution()
print(s.mySqrt(1))
print(s.mySqrt(2))
print(s.mySqrt(10))
print(s.mySqrt(100))
print(s.mySqrt(1000))
