import time


class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = set()
        longest_left_ix, longest_right_ix = 0, 1

        for segment_len in range(1, len(s) + 1):
            for ix in range(len(s) - segment_len + 1):
                # segment = s[ix:ix + segment_len]

                # 1 check if palindrome
                is_p = False
                if segment_len == 1:
                    is_p = True
                elif segment_len == 2:
                    is_p = s[ix] == s[ix + 1]
                    if is_p:
                        memo.add((ix, ix + segment_len))
                else:
                    ends_same = s[ix] == s[ix + segment_len - 1]
                    interior_is_p = (ix + 1, ix + segment_len - 1) in memo or segment_len == 3
                    is_p = ends_same and interior_is_p
                    if is_p:
                        memo.add((ix, ix + segment_len))

                # if palindrome update longest ix-es
                if is_p:
                    if segment_len  > longest_right_ix - 1 - longest_left_ix:
                        longest_left_ix, longest_right_ix = ix, ix + segment_len

        return s[longest_left_ix:longest_right_ix]


so = Solution()
# print(so.longestPalindrome("cbbd"))
# print(so.longestPalindrome("abc"))
# print(so.longestPalindrome("abcdc"))
# print(so.longestPalindrome(""))
# print(so.longestPalindrome("a"))
# print(so.longestPalindrome("dvd"))
# print(so.longestPalindrome("abcdvd"))
# print(so.longestPalindrome("abcedvdee"))
s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
#s = "ccccc"
start_time = time.time()
c = so.longestPalindrome(s)
print(len(c))
print(len(c) == len(s))
print("--- %s seconds ---" % (time.time() - start_time))
