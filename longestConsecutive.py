from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss = set(nums)
        max_len = 0
        for num in nums:
            if num -1 not in numss:
                num_in_seq = num + 1
                current_len = 1
                while num_in_seq in numss:
                    num_in_seq += 1
                    current_len += 1
                max_len = max(max_len, current_len)

        return max_len



nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))
