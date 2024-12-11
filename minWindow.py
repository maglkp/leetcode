class Solution:
    def minWindow(self, s: str, t: str) -> str:

        chars = dict()
        for char in t:
            chars[char] = chars.get(char, 0) + 1
        positive_chars_counts_sum = sum(chars.values())

        left, right = 0, 0
        min_window = None

        while right < len(s) or left < len(s):
            # if entire subsequence is found advance left pointer, remove first char from dict
            if positive_chars_counts_sum == 0:
                if min_window is None or right - left < len(min_window):
                    min_window = s[left:right]

                if s[left] in chars:
                    chars[s[left]] += 1
                    if chars[s[left]] > 0: # should always be true?
                        positive_chars_counts_sum += 1
                left += 1
            else:
                # otherwise advance right pointer, increment last char to dict if it exists and is positive
                if s[right] in chars:
                    chars[s[right]] -= 1
                    if chars[s[right]] >= 0:
                        positive_chars_counts_sum -= 1
                right += 1

            if positive_chars_counts_sum == 0:
                if min_window is None or right - left < len(min_window):
                    min_window = s[left:right]

            if right == len(s) and positive_chars_counts_sum > 0:
                break

        return min_window if min_window is not None else ""


s = Solution()
st = "ADOBECODEBANC"
t = "ABC"
print(s.minWindow(st, t))


