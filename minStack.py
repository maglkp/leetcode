from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            min_val = min(self.stack[-1][1], val)
            self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)
print(param_4)
