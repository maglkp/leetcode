from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.create_trie(words)
        m = len(board)
        n = len(board[0])
        words_found = set()
        visited = set()

        def dfs(i, j, sub_trie, word):
            if "is_real_word" in sub_trie:
                words_found.add(word)

            neis = list(filter(lambda x: x not in visited, self.get_neighbors(m, n, i, j)))
            for nei in neis:
                next_char = board[nei[0]][nei[1]]
                if next_char in sub_trie:
                    visited.add(nei)
                    dfs(nei[0], nei[1], sub_trie[next_char], word + next_char)
                    visited.remove(nei)

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    visited.clear()
                    visited.add((i, j))
                    sub_trie = trie[board[i][j]]
                    dfs(i, j, sub_trie, board[i][j])

        return list(words_found)

    def get_neighbors(self, m, n, i, j):
        neighbors = []
        if i < m - 1:
            neighbors.append((i + 1, j))
        if i > 0:
            neighbors.append((i - 1, j))
        if j < n - 1:
            neighbors.append((i, j + 1))
        if j > 0:
            neighbors.append((i, j - 1))
        return neighbors

    def create_trie(self, words):
        trie = {}
        for word in words:
            current = trie
            for c in word:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current["is_real_word"] = True

        return trie


board = [["a", "b"], ["c", "d"]]
words = ["ab"]
words = ["abcd"]

board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
s = Solution()
print(s.findWords(board, words))
