from typing import List
from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        pairs = defaultdict(list)

        # first create a map of 2sum -> map of unique pairs of indices (index -> count)
        # it will naturally be unique combinations due to how we iterate
        for i in range(n):
            for j in range(i + 1, n):
                # no need to sort as i < j
                pairs[nums[i] + nums[j]].append([i, j])

        # iterate over values of values
        complements_seen = set()
        quads = set()
        for sum2_key in pairs:
            complement = target - sum2_key
            if complement not in pairs:
                continue

            if complement == sum2_key:
                selfs_list = pairs[sum2_key]
                for i in range(len(selfs_list)):
                    for j in range(i + 1, len(selfs_list)):
                        if not (selfs_list[i][0] in selfs_list[j] or selfs_list[i][1] in selfs_list[j]):
                            s = sorted([selfs_list[i][0], selfs_list[i][1], selfs_list[j][0], selfs_list[j][1]])
                            quads.add((s[0], s[1], s[2], s[3]))
            else:
                if complement not in complements_seen:
                    for base_pair in pairs[sum2_key]:
                        # causes "dictionary changed size during iteration"
                        # for complement_pair in pairs[complement]:
                        for complement_pair in pairs.get(complement, []):
                            # don't add quads that same number repeated (ie triples)
                            if not (base_pair[0] in complement_pair or base_pair[1] in complement_pair):
                                s = sorted(
                                    [int(base_pair[0]), int(base_pair[1]), int(complement_pair[0]),
                                     int(complement_pair[1])])
                                quads.add((s[0], s[1], s[2], s[3]))

                complements_seen.add(sum2_key)

        # quads is a set of sets
        quad_vals = set()
        for q in quads:
            vals = sorted([
                nums[q[0]],
                nums[q[1]],
                nums[q[2]],
                nums[q[3]]
            ])
            # quad_vals.add(tuple(vals))

            quad_vals.add((int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3])))
        return [list(a) for a in quad_vals]


# nums = [1, 0, -1, 0, -2, 2]
# target = 0
nums = [2, 2, 2, 2, 2]
target = 8

nums = [1, 1]
target = 2

nums = [-5, 5, 4, -3, 0, 0, 4, -2]
target = 4

nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
target = 8
s = Solution()
print(s.fourSum(nums, target))
