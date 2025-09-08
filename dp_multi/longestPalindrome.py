# https://leetcode.com/problems/longest-substring-without-repeating-characters/
import time

class Solution:

    def longestPalindrome(self, s: str) -> str:
        longest_left, longest_right = 0, 0
        for i in range(len(s)):
            p1 = self.expandAroundPivot(i, i, s)
            p2 = self.expandAroundPivot(i, i + 1, s)
            palindrome_len = max(p1, p2)
            if palindrome_len > longest_right - longest_left + 1:
                l = i - int((palindrome_len - 1) / 2)
                r = i + int(palindrome_len / 2)
                longest_left, longest_right = l, r

        return s[longest_left:longest_right + 1]


    # returns length of the palindrome around pivot
    def expandAroundPivot(self, left: int, right: int, s: str) -> int:
        if right > len(s) - 1:
            return 0
        if s[left] != s[right]:
            return 0
        while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
        return right - left + 1


def longestPalindromeCubic(s: str) -> str:
    longest_left, longest_right = 0, 1
    len_s = len(s)
    for left in range(len_s):
        if len_s - left > longest_right - longest_left:
            for right in range(left + 1, len_s + 1):
                if isPalindrome(s[left:right]) and right - left > longest_right - longest_left:
                    longest_left, longest_right = left, right
    return s[longest_left:longest_right]


def isPalindrome(s: str) -> bool:
    i = 0
    half_len_ix = int(len(s) / 2)
    last_ix = len(s) - 1
    while i < half_len_ix:
        if s[i] != s[last_ix - i]:
            return False
        i += 1
    return True

so = Solution()
print(so.longestPalindrome("cbbd"))
print(so.longestPalindrome("abc"))
print(so.longestPalindrome("abcdc"))
print(so.longestPalindrome(""))
print(so.longestPalindrome("a"))
print(so.longestPalindrome("dvd"))
print(so.longestPalindrome("abcdvd"))
print(so.longestPalindrome("abcedvdee"))

start_time = time.time()
print(so.longestPalindrome(
    "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"))
print("--- %s seconds ---" % (time.time() - start_time))
