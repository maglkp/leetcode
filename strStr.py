from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_ix = 0
        haystack_ix = 0
        while haystack_ix < len(haystack):
            if haystack[haystack_ix] == needle[needle_ix]:
                if needle_ix == len(needle) - 1:
                    return haystack_ix - needle_ix
                else:
                    needle_ix += 1

                haystack_ix += 1
            else:
                haystack_ix -= needle_ix - 1
                needle_ix = 0


        return -1


s = Solution()
haystack = "mississippi"
needle = "issip"
k = s.strStr(haystack, needle)
print(k)
