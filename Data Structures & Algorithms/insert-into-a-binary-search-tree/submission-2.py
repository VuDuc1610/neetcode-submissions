# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        temp = root
        def helper(node):
            if not node:
                return None
            if not node.left and node.val > val:
                node.left = TreeNode(val)
            if not node.right and node.val < val:
                node.right = TreeNode(val)
            elif node.val < val:
                helper(node.right)
            else:
                helper(node.left)
        helper(temp)
        return root

