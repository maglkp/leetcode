# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# use the same set that does not reset, only grow and shrink it as needed
def lengthOfLongestSubstring(s: str) -> int:
    longest_len = 0
    current = set()
    left = 0
    right = 0

    while right < len(s):
        c = s[right]
        if c in current:
            if len(current) > longest_len:
                longest_len = len(current)
            current.remove(s[left])
            left += 1
        else:
            right += 1
            current.add(c)

    if len(current) > longest_len:
        longest_len = len(current)

    return longest_len

def lengthOfLongestSubstringSlowWithReset(s: str) -> int:
    longest_len = 0
    current = set()
    anchor = 0
    ix = 0

    while ix < len(s):
        c = s[ix]
        if c in current:
            if len(current) > longest_len:
                longest_len = len(current)
            current = set()
            ix = anchor + 1
            anchor = ix
        else:
            ix += 1
            current.add(c)

    if len(current) > longest_len:
        longest_len = len(current)

    return longest_len


print(lengthOfLongestSubstring("dvdf"))
