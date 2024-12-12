class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = dict()
        for s in s:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        for t in t:
            if t not in d:
                return False
            else:
                d[t] -= 1
                if d[t] < 0:
                    return False
        return True