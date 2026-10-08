# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        leftSide = self.lowestCommonAncestor(root.left, p, q)
        rightSide = self.lowestCommonAncestor(root.right, p, q)
        if (leftSide == p and rightSide == q) or (rightSide == p and leftSide == q):
            return root
        else:
            return leftSide or rightSide
        