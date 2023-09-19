from typing import List


def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    best_closest = nums[0] + nums[1] + nums[2]

    for ix, num in enumerate(nums):
        nums_rest = nums[ix + 1:]
        if len(nums_rest) < 2:
            continue
        current_closest = twoSum("", nums_rest, target, nums[ix])
        if abs(current_closest - target) < abs(best_closest - target):
            best_closest = current_closest
    return best_closest


def twoSum(self, numbers: List[int], target: int, current: int) -> int:
    left, right = 0, len(numbers) - 1

    current_closest = numbers[left] + numbers[right] + current
    while left < right:
        candidate = numbers[left] + numbers[right] + current
        if abs(candidate - target) < abs(current_closest - target):
            current_closest = candidate
        if candidate > target:
            right -= 1
        else:
            left += 1
    return current_closest

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest("", nums, target))