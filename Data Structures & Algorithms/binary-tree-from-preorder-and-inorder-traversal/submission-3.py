# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        count = 0
        myMap = {}
        for i in range(len(inorder)):
            myMap[inorder[i]] = i
        
        def helper(left, right):
            nonlocal count
            if left > right:
                return
            nodeVal = preorder[count]
            node = TreeNode(nodeVal)
            count += 1

            mid = myMap[nodeVal]

            node.left = helper(left, mid-1)
            node.right = helper(mid+1, right)
            return node

        return helper(0, len(inorder)-1)