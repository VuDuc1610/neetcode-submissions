# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans, temp = 0, 0

        def helper(root, temp):
            nonlocal ans
            if not root:
                return 
            temp *= 10
            temp += root.val

            if not root.left and not root.right:
                ans += temp
                return
            helper(root.left, temp)
            helper(root.right, temp)
        
        helper(root, 0)

        return ans