from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTreeInterative(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # active = root

        ## loop
        # take next element from preorder next_1

        # if next_1 is on the left side or active create L node, set L = True
        # otherwise create R node, set L = False

        # take next element from preorder next_2
        # if L and next_2 is on the right side of active create R node, set active to R, continue
        # otherwise
        pass

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        active = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1 + active], inorder[:active])
        root.right = self.buildTree(preorder[active+ 1:], inorder[active + 1:])

        return root
