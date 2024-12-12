from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        window_size = min(k + 1, len(nums))
        for ix in range(window_size):
            if nums[ix] in window:
                return True
            window.add(nums[ix])

        for ix in range(window_size, len(nums)):
            window.remove(nums[ix - window_size])
            if nums[ix] in window:
                return True
            window.add(nums[ix])

        return False


nums = [1, 2, 3, 1]
k = 3
s = Solution()
print(s.containsNearbyDuplicate(nums, k))
