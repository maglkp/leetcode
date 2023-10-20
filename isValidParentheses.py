from typing import Dict
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        q = []
        while len(s) > 0:
            bracket = s.pop(0)
            if bracket in ['{', '(', '[']:
                q.append(bracket)
            else:
                if len(q) == 0:
                    return False

                left = q.pop()
                if ((bracket == '}' and left != '{') or
                        (bracket == ')' and left != '(') or
                        (bracket == ']' and left != '[')):
                    return False
        return len(q) == 0


s = Solution()
print(s.isValid("]"))
