from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        for p in path.split("/"):
            if p == ".":
                pass
            elif p == "..":
                if stack:
                    stack.pop()
            elif p:
                stack.append(p)
        return "/" + "/".join(stack)


s = Solution()
p = "/../.../a/../b/c/../d/./"
print(s.simplifyPath(p))