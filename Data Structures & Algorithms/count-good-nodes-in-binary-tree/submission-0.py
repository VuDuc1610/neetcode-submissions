# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def helper(root, currMax):
            nonlocal count
            if not root:
                return
            if root.val >= currMax:
                count += 1
                currMax = root.val
            helper(root.left, currMax)
            helper(root.right, currMax)
        
        helper(root, root.val)
        return count
            

        