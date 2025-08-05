from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        trie = {}

        for word in wordDict:
            current = trie
            for c in word:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current["is_real_word"] = True

        dp = {}
        return self.word_break_dp(s, trie, dp)

    def word_break_dp(self, s: str, trie: dict, dp: dict) -> bool:

        if not s:
            return True

        if len(s) in dp:
            return dp[len(s)]

        # find all words in word_dict that are prefixes of s
        level = trie
        words = []
        for ix in range(len(s)):
            c = s[ix]
            if c not in level:
                break
            level = level[c]
            # one can try word immediately to avoid unnecessary memory usage
            if "is_real_word" in level:
                words.append(s[:ix + 1])

        for word in reversed(words):
            if self.word_break_dp(s[len(word):], trie, dp):
                dp[len(s)] = True
                return True
            else:
                dp[len(s)] = False

        return False


st = "leetcode"
wordDict = ["leet", "code"]
st = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

s = Solution()
print(s.wordBreak(st, wordDict))
