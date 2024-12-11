class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Given a pattern and a string s, find if s follows the same pattern.
        # Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
        # - Each letter in pattern maps to exactly one unique word in s.
        # - Each unique word in s maps to exactly one letter in pattern.
        # - No two letters map to the same word, and no two words map to the same letter.

        # split the s into words

        # create a map of letter -> word
        # create a set of 'words' which are the words already in the map

        d = dict()
        words = set()
        input = s.split()
        if len(input) != len(pattern):
            return False
        for i in range(len(pattern)):
            word = input[i]
            letter = pattern[i]
            if letter not in d:
                if word in words:
                    return False
                words.add(word)
                d[letter] = word
            elif d[letter] != word:
                return False

        return True


pattern = "abba"
s1 = "dog cat cat dog"
pattern = "aaa"
s1 = "aa aa aa aa"
s = Solution()

print(s.wordPattern(pattern, s1))