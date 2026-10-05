# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        minNum, maxNum = float('-inf'), float('inf')

        def helper(root, minNum, maxNum):
            nonlocal ans
            if not root:
                return
            if root.val <= minNum or root.val >= maxNum:
                ans = False
                return
            
            helper(root.left, minNum, root.val)
            helper(root.right, root.val, maxNum)
        
        helper(root.left, minNum, root.val)
        helper(root.right, root.val, maxNum)

        return ans
        
            