class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diags1 = set()
        diags2 = set()
        ct = [0]

        def add_queen_in_row_dfs(row: int):
            if row == n:
                ct[0] += 1
                return

            for col in range(n):
                if col not in cols and row + col not in diags1 and row - col not in diags2:
                    cols.add(col)
                    diags1.add(row + col)
                    diags2.add(row - col)
                    add_queen_in_row_dfs(row + 1)
                    cols.remove(col)
                    diags1.remove(row + col)
                    diags2.remove(row - col)

        add_queen_in_row_dfs(0)
        return ct[0]


s = Solution()
for i in range(1, 27):
    print("i = " + str(i) + ", totalNQueens = " + str(s.totalNQueens(i)))