class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.min_distance_dp(word1, word2, {})

    def min_distance_dp(self, word1: str, word2: str, memo: dict) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if (word1, word2) in memo:
            return memo[(word1, word2)]

        if word1[0] == word2[0]:
            dist = self.min_distance_dp(word1[1:], word2[1:], memo)
            memo[(word1, word2)] = dist
            return dist

        dist1 = 1 + self.min_distance_dp(word1, word2[1:], memo)
        dist2 = 1 + self.min_distance_dp(word1[1:], word2, memo)
        dist3 = 1 + self.min_distance_dp(word1[1:], word2[1:], memo)
        dist = min(dist1, dist2, dist3)
        memo[(word1, word2)] = dist
        return dist
