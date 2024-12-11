class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        values = set()
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in values:
                    return False
                values.add(t[i])
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
        return True



s1 = "badc"
t =  "baba"

s = Solution()
print(s.isIsomorphic(s1, t))