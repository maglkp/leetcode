from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [True] + [False] * len(s)
        words = set(wordDict)

        for i in range(1, len(dp)):
            for j in range(i):
                candidate_word = s[j:i]
                if dp[j] and candidate_word in words:
                    dp[i] = True
                    break

        return dp[-1]



st = "leetcode"
wordDict = ["leet", "code"]
st = "catsandog"
wordDict = ["cats", "dog", "sand", "an", "cat"]

#st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
#wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

s = Solution()
print(s.wordBreak(st, wordDict))
