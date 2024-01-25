from typing import List


class Solution:

    def __init__(self):
        self.box_size = 3
        self.row_size = 9
        self.box_index = lambda row, col: (row // self.box_size) * self.box_size + col // self.box_size

        self.rows = [set() for _ in range(self.row_size)]
        self.columns = [set() for _ in range(self.row_size)]
        self.boxes = [set() for _ in range(self.row_size)]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(self.row_size):
            for j in range(self.row_size):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    self.place_number(d, i, j, board)

        self.solveWithBackTracking(board)

    def solveWithBackTracking(self, board: List[List[str]]) -> bool:
        row, col = self.findUnassignedLocation(board)
        if row == -1 and col == -1:
            return True

        for num in range(1, 10):
            if self.can_place_number(num, row, col):
                self.place_number(num, row, col, board)
                if self.solveWithBackTracking(board):
                    return True
                self.remove_number(num, row, col, board)

        return False

    def findUnassignedLocation(self, board: List[List[str]]):
        for row in range(self.row_size):
            for col in range(self.row_size):
                if board[row][col] == '.':
                    return row, col
        return -1, -1

    # def solveSudokuBackTrack(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #
    #     for i in range(self.row_size):
    #         for j in range(self.row_size):
    #             if board[i][j] != '.':
    #                 d = int(board[i][j])
    #                 self.place_number(d, i, j)
    #
    #     self.backtrackWithManualPrevNumberIncrement(0, 0, 1, board)

    def previous_cell(self, row, col):
        if col == 0:
            return row - 1, self.row_size - 1
        else:
            return row, col - 1

    def next_cell(self, row, col):
        if col == self.row_size - 1:
            return row + 1, 0
        else:
            return row, col + 1

    # def backtrackWithManualPrevNumberIncrement(self, row, col, start_ix, board):
    #     # if last cell and already has a number it means the only solution is found
    #     if board[row][col] != "." and row == self.row_size - 1 and col == self.row_size - 1:
    #         return
    #
    #     # if this cell already has a number go to next cell
    #     if board[row][col] != ".":
    #         next_row, next_col = self.next_cell(row, col)
    #         self.backtrack(next_row, next_col, 1, board)
    #
    #     if start_ix == 10:
    #         prev_row, prev_col = self.previous_cell(row, col)
    #         prev_num = int(board[prev_row][prev_col])
    #         self.remove_number(prev_num, prev_row, prev_col)
    #         self.backtrack(prev_row, prev_col, prev_num + 1, board)
    #         return
    #
    #     placed = False
    #     for i in range(start_ix, 10):
    #         if self.can_place_number(i, row, col):
    #             # place number and go to next
    #             self.place_number(i, row, col)
    #             placed = True
    #             break
    #
    #     # if not placed backtrack to previous cell
    #     if not placed:
    #         # remove previous number
    #         prev_row, prev_col = self.previous_cell(row, col)
    #         prev_num = int(board[prev_row][prev_col])
    #         self.remove_number(prev_num, prev_row, prev_col)
    #         self.backtrack(prev_row, prev_col, prev_num + 1, board)
    #         return
    #
    #     # if placed and last cell - return
    #     if row == self.row_size - 1 and col == self.row_size - 1:
    #         return
    #
    #     # else go to next cell
    #     next_row, next_col = self.next_cell(row, col)
    #     self.backtrack(next_row, next_col, 1, board)

    def remove_number(self, d, row, col, board):
        """
        Remove a number that didn't lead
        to a solution
        """
        self.rows[row].remove(d)
        self.columns[col].remove(d)
        self.boxes[self.box_index(row, col)].remove(d)
        board[row][col] = '.'

    def can_place_number(self, d, row, col):
        return d not in self.rows[row] and \
            d not in self.columns[col] and \
            d not in self.boxes[self.box_index(row, col)]

    def place_number(self, d, row, col, board):
        self.rows[row].add(d)
        self.columns[col].add(d)
        self.boxes[self.box_index(row, col)].add(d)
        board[row][col] = str(d)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s = Solution()
s.solveSudoku(board)
print(board)
