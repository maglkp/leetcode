from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions: List[str] = []
        self.iterate(n, 0, solutions, "")
        return solutions

    def iterate(self, parensToOpen: int, parensToClose: int, solutions: List[str], acc: str):
        if (parensToOpen, parensToClose) == (0, 0):
            solutions.append(acc)
            return
        if parensToOpen > 0 and parensToClose == 0:
            self.iterate(parensToOpen - 1, parensToClose + 1, solutions, acc + "(")
        elif parensToOpen == 0 and parensToClose > 0:
            self.iterate(parensToOpen, parensToClose - 1, solutions, acc + ")")
        else:
            self.iterate(parensToOpen - 1, parensToClose + 1, solutions, acc + "(")
            self.iterate(parensToOpen, parensToClose - 1, solutions, acc + ")")

s = Solution()
print(s.generateParenthesis(4))
