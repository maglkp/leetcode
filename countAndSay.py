from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"
        if n == 2:
            return "11"

        curr = [(1, 1)]
        new = []

        for i in range(n - 2):
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
            curr = new

        return str(new)

    def countAndSayIdiomatic(self, n: int) -> str:
        if n == 1:
            return "1"

        curr = "1"

        for _ in range(n - 1):
            next_val = []
            count = 1

            for j in range(1, len(curr)):
                if curr[j] == curr[j - 1]:
                    count += 1
                else:
                    next_val.append(str(count))
                    next_val.append(curr[j - 1])
                    count = 1

            # Flush the final sequence
            next_val.append(str(count))
            next_val.append(curr[-1])

            curr = "".join(next_val)

        return curr


s = Solution()
n = 3
print(s.countAndSay(n))
