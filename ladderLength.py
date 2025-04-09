from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def is_diff_1(word1, word2):
            diffs = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diffs += 1
            return diffs == 1

        banksy = set(wordList)
        q = deque()
        visited = set()

        q.append((beginWord, 1))
        while q:
            current_gene, step = q.popleft()
            if current_gene == endWord:
                return step
            visited.add(current_gene)
            for next_gene in banksy:
                if is_diff_1(next_gene, current_gene) and next_gene not in visited:
                    q.append((next_gene, step + 1))

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
print(s.ladderLength(beginWord, endWord, wordList))
