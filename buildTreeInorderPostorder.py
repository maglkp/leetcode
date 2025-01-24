from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        root = TreeNode(postorder[-1])
        active = inorder.index(root.val)
        root.left = self.buildTree(inorder[:active], postorder[:active])
        root.right = self.buildTree(inorder[active + 1:], postorder[active:-1])
        return root
