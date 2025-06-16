from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, visited, word):
            if board[i][j] == word[0]:
                if len(word) == 1:
                    return True
                visited.add((i, j))
                for nei in self.get_neighbors(m, n, i, j):
                    if nei not in visited and dfs(nei[0], nei[1], visited, word[1:]):
                        return True
                visited.remove((i, j))

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, set(), word):
                    return True

        return False

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


s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(s.exist(board, word))
