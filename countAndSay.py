from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        curr = [(1, 1)]
        new = []

        for i in range(n - 2):
            curr = new
            new = []
            acc = 0
            for j in range(len(curr) + 1):
                if j == 0:
                    acc = curr[j][0]
                elif j == len(curr):
                    k = acc + curr[j - 1][0]
                    v = curr[j - 1][1]
                    new.append((1, k))
                    new.append((1, v))
                else:
                    if curr[j][1] == curr[j - 1][1]:
                        acc += curr[j - 1][0]
                    else:
                        k = acc + curr[j - 1][0]
                        v = curr[j - 1][1]
                        new.append((1, k))
                        new.append((1, v))
                        acc = 0
                        # acc = curr[j][1]

        return str(new)



s = Solution()
n = 3
print(s.countAndSay(n))
