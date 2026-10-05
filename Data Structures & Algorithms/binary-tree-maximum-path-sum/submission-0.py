# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def helper(root):
            nonlocal ans
            if not root:
                return 0
            leftTree = helper(root.left)
            rightTree = helper(root.right)
            
            leftTree = max(leftTree,0)
            rightTree = max(rightTree,0)

            ans = max(root.val + leftTree + rightTree, ans)

            return root.val + max(leftTree, rightTree)
        
        helper(root)
        return ans
