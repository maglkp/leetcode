# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum(root, [])

    def sum(self, node: Optional[TreeNode], path: List[int]) -> int:
        if not node:
            return 0

        if not node.left and not node.right:
            return self.num(path + [node.val])

        return self.sum(node.left, path + [node.val]) + self.sum(node.right, path + [node.val])

    def num(self, path: List[int]) -> int:
        n = len(path)
        return sum(digit * (10 ** (n - i - 1)) for i, digit in enumerate(path))


