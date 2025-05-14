from typing import List, Set


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set9 = set()
        for i in range(1, 10):
            set9.add(str(i))

        # validate horizontal rows
        for row in board:
            if not self.set_is_valid(row, set9):
                return False

        # validate vertical columns
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if not self.set_is_valid(column, set9):
                return False

        for i in range(3):
            for j in range(3):
                square = []
                for k in range(3):
                    for l in range(3):
                        square.append(board[i * 3 + k][j * 3 + l])
                if not self.set_is_valid(square, set9):
                    return False

        return True

    def set_is_valid(self, nums: List[str], set9: Set) -> bool:
        current_set = set(set9)
        for num in nums:
            if num == ".":
                continue
            if num in current_set:
                current_set.remove(num)
            else:
                return False
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


s = Solution()
print(s.isValidSudoku(board))