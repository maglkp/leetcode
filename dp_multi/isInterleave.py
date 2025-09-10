# using constant O(1) space only :)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.is_interleave_dp(s1, s2, s3, 0, 0, 0, set())


    def is_interleave_dp(self, s1: str, s2: str, s3: str, s1_idx: int, s2_idx: int, s3_idx: int, bad_paths: set) -> bool:
        if s1_idx == len(s1) and s2_idx == len(s2):
            return True

        # if either s1 or s2 was exhausted and the other was not
        # check if remaining matches what's left in s3
        if s1_idx == len(s1):
            ok = s2[s2_idx:] == s3[s3_idx:]
            if not ok:
                bad_paths.add((s1_idx, s2_idx))
            return ok
        if s2_idx == len(s2):
            ok = s1[s1_idx:] == s3[s3_idx:]
            if not ok:
                bad_paths.add((s1_idx, s2_idx))
            return ok

        if (s1_idx, s2_idx) in bad_paths:
            return False

        c1 = s1[s1_idx]
        c2 = s2[s2_idx]
        c3 = s3[s3_idx]

        if c1 != c3 and c2 != c3:
            return False

        if c1 == c3:
            take_from_s1 = self.is_interleave_dp(s1, s2, s3, s1_idx + 1, s2_idx, s3_idx + 1, bad_paths)
            if not take_from_s1:
                bad_paths.add((s1_idx + 1, s2_idx))
            else:
                return True
        if c2 == c3:
            take_from_s2 = self.is_interleave_dp(s1, s2, s3, s1_idx, s2_idx + 1, s3_idx + 1, bad_paths)
            if not take_from_s2:
                bad_paths.add((s1_idx, s2_idx + 1))
            else:
                return True

        bad_paths.add((s1_idx, s2_idx))
        return False


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s = Solution()
print(s.isInterleave(s1, s2, s3))