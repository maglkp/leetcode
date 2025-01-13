from typing import List
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token == "+":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left + right)
            elif token == "-":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left - right)
            elif token == "*":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left * right)
            elif token == "/":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left / right)
            else:
                stack.append(token)

        return int(stack[0])


s = Solution()
d = ["2", "1", "+", "3", "*"]
d = ["4", "13", "5", "/", "+"]
d = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(s.evalRPN(d))
