# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True

        def helper(root):
            nonlocal balance
            if not root:
                return 0
            leftSide = helper(root.left)
            rightSide = helper(root.right)
            if abs(leftSide-rightSide) >= 2:
                balance = False
            return 1 + max(leftSide, rightSide)
        
        helper(root)
        return balance