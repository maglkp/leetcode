from typing import List


class Solution:

    def reverse_subarray(self, s: List, start: int, end: int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def find_next_word_boundaries(self, s: List, start_ix: int) -> (int, int):
        while start_ix < len(s) and s[start_ix] == ' ':
            start_ix += 1
        end_ix = start_ix
        while end_ix < len(s) and s[end_ix] != ' ':
            end_ix += 1
        return start_ix, end_ix

    def reverseWords(self, s: str) -> str:
        t = list(s)

        # find the indexes of first and last non-whitespace characters
        start_ix = 0
        while start_ix < len(t) and t[start_ix] == ' ':
            start_ix += 1
        end_ix = len(t) - 1
        while end_ix >= 0 and t[end_ix] == ' ':
            end_ix -= 1

        t = t[start_ix: end_ix + 1]
        # reverse the whole string
        self.reverse_subarray(t, 0, len(t) - 1)
        # starting at index 0 find next word boundary, reverse it and continue until end of string
        start_ix = 0
        while start_ix < len(t):
            start_ix, end_ix = self.find_next_word_boundaries(t, start_ix)
            self.reverse_subarray(t, start_ix, end_ix - 1)
            start_ix = end_ix
        return ''.join(t)


st = "  the sky is blue  "
s = Solution()
print(s.reverseWords(st))
