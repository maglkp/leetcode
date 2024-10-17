from typing import List, Set, Dict


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [0] * n

        acc = 1
        # set products array to product of each element in nums to the left of it
        for ix in range(n):
            products[ix] = acc
            acc *= nums[ix]

        # compute the product of each element in nums to the right of it
        # multiply each element in products array to the right of it
        acc = 1
        for ix in reversed(range(n)):
            products[ix] *= acc
            acc *= nums[ix]

        return products


s = Solution()
nums = [1, 2, 3, 4]
print(s.productExceptSelf(nums))
