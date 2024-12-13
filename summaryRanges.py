from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        ranges = []
        start_ix = 0
        for ix in range(1, len(nums)):
            if nums[ix] - 1 != nums[ix - 1]:
                if ix - start_ix == 1:
                    ranges.append(str(nums[start_ix]))
                else:
                    ranges.append(str(nums[start_ix]) + "->" + str(nums[ix - 1]))
                start_ix = ix
            if ix == len(nums) - 1:
                if ix - start_ix == 0:
                    ranges.append(str(nums[start_ix]))
                else:
                    ranges.append(str(nums[start_ix]) + "->" + str(nums[ix]))

        return ranges


nums = [0, 1, 2, 4, 5, 7, 8]

s = Solution()
print(s.summaryRanges(nums))
