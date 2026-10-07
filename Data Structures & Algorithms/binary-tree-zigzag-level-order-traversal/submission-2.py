# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        leftToRight = True
        if not root:
            return ans
        q = deque([root])

        while q:
            level = deque()
            for _ in range(len(q)):
                curr = q.popleft()
                if leftToRight:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            leftToRight = not leftToRight
            ans.append(level)
            
        return ans