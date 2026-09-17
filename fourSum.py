from typing import List
from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        pairs = defaultdict(dict)

        # first create a map of 2sum -> map of unique pairs of indices (index -> count)
        # it will naturally be unique combinations due to how we iterate
        for i in range(n):
            for j in range(i + 1, n):
                # inner map of pair -> count of occurrences
                count_map = pairs[nums[i] + nums[j]]
                # v1, v2 = (i, j) if nums[i] < nums[j] else (nums[j], nums[i])
                # no need to sort as i < j
                if (i, j) not in count_map:
                    count_map[(i, j)] = 1
                else:
                    count_map[(i, j)] += 1

        # iterate over values of values
        complements_seen = set()
        quads = set()
        for sum2_key in pairs:
            complement = target - sum2_key
            if complement == sum2_key:
                map_for_self_complementing = pairs[sum2_key]
                for pair in map_for_self_complementing:
                    if map_for_self_complementing[pair] > 1 :
                        s = sorted([pair[0], pair[1], pair[0], pair[1]])
                        quads.add((s[0], s[1], s[2], s[3]))
            else:
                if complement not in complements_seen:
                    for base_pair in pairs[sum2_key]:
                        for complement_pair in pairs[complement]:
                            # don't add quads that same number repeated (ie triples)
                            if not (base_pair[0] in complement_pair or base_pair[1] in complement_pair):
                                s = sorted(
                                    [int(nums[base_pair[0]]), int(nums[base_pair[1]]), int(nums[complement_pair[0]]),
                                     int(nums[complement_pair[1]])])
                                quads.add((s[0], s[1], s[2], s[3]))

                complements_seen.add(sum2_key)

        return [list(a) for a in quads]


nums = [1, 0, -1, 0, -2, 2]
target = 0
nums = [2, 2, 2, 2, 2]
target = 8
s = Solution()
print(s.fourSum(nums, target))
