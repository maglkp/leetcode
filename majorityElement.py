from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pass



nums = [1, 1, 1, 2, 2]
s = Solution()
#print(s.majorityElement(nums))

num = -12


out = ""
for bit_ix in range(32):
    out = str((num >> bit_ix) & 1) + out


print(out)

#vv = 0b11111111111111111111111111110100
#print(vv)



