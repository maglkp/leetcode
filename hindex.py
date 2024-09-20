from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c_counts = [0] * len(citations)
        for c in citations:
            if c > 0:
                c_norm = min(c - 1, len(c_counts) - 1)
                c_counts[c_norm] += 1

        cumulative_c_count = 0
        for ix in reversed(range(len(c_counts))):
            if c_counts[ix] + cumulative_c_count >= (ix + 1):
                return ix + 1
            else:
                cumulative_c_count += c_counts[ix]

        return 0


s = Solution()
citations = [3, 0, 6, 1, 5]
print(s.hIndex(citations))
