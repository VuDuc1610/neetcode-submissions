# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(root):
            nonlocal ans
            if not root:
                return 0
            root.left = helper(root.left)
            root.right = helper(root.right)
            ans = max(ans, 1 + root.left + root.right)

            return 1 + max(root.left, root.right)
        
        helper(root)
        return ans - 1