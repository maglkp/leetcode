from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        # for every string sort it and create a hash value for it
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in d:
                d[sort_s].append(s)
            else:
                d[sort_s] = [s]

        return list(map(lambda a: a[1], d.items()))


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))
