from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        write_ix = 0
        last_value = None

        for element in nums:
            if last_value != element:
                last_value = element
                nums[write_ix] = element
                write_ix += 1

        return write_ix


s = Solution()
haystack = "sadbutsad"
needle = "sad"
k = s.strStr(haystack, needle)
print(k)
