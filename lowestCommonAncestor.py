# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Create a path to root for p and q
# Reverse it, find last element of longest common prefix
# Time 2*O(h) | Space 2*O(h)

# Create a path to root for p, put all elements in set
# Traverse q to top, for every element check if it's in set
# Time 2*O(h) | Space O(h)

# DFS and check if right or left subtree has p and/or q
# if p or q is found, propagate that node
# if p and q is found in both l and r subtrees then it's the LCA, propagate that node
# if only one of p,q is found in l,r subtrees then propagate that subtree's node

# Time O(n) | Space O(1)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r



