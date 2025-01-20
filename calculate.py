from typing import List
from collections import deque
import re


class Solution:

    def calculate(self, s: str) -> int:
        s = re.split(r'(\d+)|(\s+)|(\+)|(-)|(\()|(\))', s)
        s = [i for i in s if i and not i.isspace()]

        ix = 0
        stack = deque()
        while ix < len(s):
            if s[ix] == ')':
                ix += 1
            elif s[ix].isdigit():
                stack.append(s[ix])
                ix += 1
            elif s[ix] == '(':
                value, ix_inc = self.eval(s[ix + 1:])
                stack.append(value)
                ix += ix_inc + 1
            elif s[ix] == '-':
                if not stack:
                    left = 0
                else:
                    left = int(stack.pop())

                if s[ix + 1].isdigit():
                    right = int(s[ix + 1])
                    stack.append(left - right)
                    ix += 2
                elif s[ix + 1] == '(':
                    right, ix_inc = self.eval(s[ix + 2:])
                    stack.append(left - int(right))
                    ix += ix_inc + 2
                else:
                    raise ValueError("Expected digit or ) after + or -")
            elif s[ix] == '+':
                left = int(stack.pop())
                if s[ix + 1].isdigit():
                    right = int(s[ix + 1])
                    stack.append(left + right)
                    ix += 2
                elif s[ix + 1] == '(':
                    right, ix_inc = self.eval(s[ix + 2:])
                    stack.append(left + int(right))
                    ix += ix_inc + 2
                else:
                    raise ValueError("Expected digit or ) after + or -")

        return int(stack.pop())

    def eval(self, s: List[str]) -> (int, int):
        ix = 0
        stack = deque()
        while ix < len(s):
            if s[ix] == ')':
                return stack.pop(), ix + 1
            elif s[ix].isdigit():
                stack.append(s[ix])
                ix += 1
            elif s[ix] == '(':
                value, ix_inc = self.eval(s[ix + 1:])
                stack.append(value)
                ix += ix_inc + 1
            elif s[ix] == '-':
                if not stack:
                    left = 0
                else:
                    left = int(stack.pop())

                if s[ix + 1].isdigit():
                    right = int(s[ix + 1])
                    stack.append(left - right)
                    ix += 2
                elif s[ix + 1] == '(':
                    right, ix_inc = self.eval(s[ix + 2:])
                    stack.append(left - int(right))
                    ix += ix_inc + 2
                else:
                    raise ValueError("Expected digit or ) after + or -")
            elif s[ix] == '+':
                left = int(stack.pop())
                if s[ix + 1].isdigit():
                    right = int(s[ix + 1])
                    stack.append(left + right)
                    ix += 2
                elif s[ix + 1] == '(':
                    right, ix_inc = self.eval(s[ix + 2:])
                    stack.append(left + int(right))
                    ix += ix_inc + 2
                else:
                    raise ValueError("Expected digit or ) after + or -")

        raise ValueError


st = "-1 + 1 - 2 - (2+3)"
st = "1 + (1+2)"
st = "(((((4)))))"
st = "1-1"
st = "(1+(4+5+2)-3)+(6+8)"
st = "0"
st = "  30"
st = "(7)-(0)+(4)"
st = "2-4-(8+2-6+(8+4-(1)+8-10))"
st = "(8+4-(1)+8-10)" # 9 ok
st = "(8+2-6+(8+4-(1)+8-10))" # 13 k
st = "(-(13))"
st = "1-(5)"
st = "(1+(4+5+2)-3)+(6+8)" # 23
st = "(9)+(14)" # we start with (), have to increase by 1 only
st = "-(8+2-6+(8+4-(1)+8-10))" # -13
st = "-(4+(12-(1)-2))" # -13 we start with operator, have to increase by +2
st = "(1+(4+5+2)-3)+(6+8)"
st = "2-4-(8+2-6+(8+4-(1)+8-10))" # -15
#st = "-(8+2-6+(8+4-(1)+8-10))" # -13
st = "(9)+(14)"
s = Solution()
print(s.calculate(st))
