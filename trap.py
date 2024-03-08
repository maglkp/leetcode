from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        total = 0
        while left < right:
            # if left is smaller increase it, otherwise decrease right
            if height[left] < height[right]:
                left += 1
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    total += max_left - height[left]
            else:
                right -= 1
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    total += max_right - height[right]

        return total


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
print(s.trap(height))
