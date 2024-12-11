class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = dict()
        for char in magazine:
            chars[char] = chars.get(char, 0) + 1

        for char in ransomNote:
            if char not in chars or chars[char] == 0:
                return False
            else:
                chars[char] -= 1

        return True