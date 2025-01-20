from typing import List
from collections import deque
import re


class Solution:

    def calculate(self, s: str) -> int:
        s = re.split(r'(\d+)|(\s+)|(\+)|(-)|(\()|(\))', s)
        s = [i for i in s if i and i != ' ']

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
            elif s[ix] == '+':
                left = int(stack.pop())
                if s[ix + 1].isdigit():
                    right = int(s[ix + 1])
                    stack.append(left + right)
                    ix += 2
                elif s[ix + 1] == '(':
                    right, ix_inc = self.eval(s[ix + 2:])
                    stack.append(left + right)
                    ix += ix_inc + 1
                else:
                    raise ValueError("Expected digit or ) after + or -")

        return stack.pop()

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
            elif s[ix] == '+':
                left = int(stack.pop())
                if s[ix + 1].isdigit():
                    right = int(s[ix + 1])
                    stack.append(left + right)
                    ix += 2
                elif s[ix + 1] == '(':
                    right, ix_inc = self.eval(s[ix + 2:])
                    stack.append(left + right)
                    ix += ix_inc + 1
                else:
                    raise ValueError("Expected digit or ) after + or -")

        raise ValueError


st = "-1 + 1 - 2 - (2+3)"
st = "1 + (1+2)"
s = Solution()
print(s.calculate(st))
