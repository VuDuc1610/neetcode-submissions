# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []

        def helper(root):
            if not root:
                ans.append("N")
                return
            ans.append(str(root.val))
            helper(root.left)
            helper(root.right)
        
        helper(root)
        s = ",".join(ans)
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        count = 0
        def helper():
            nonlocal count
            if count >= len(data) or data[count] == "N":
                count += 1
                return None
            
            node = TreeNode(data[count])
            count += 1 
            node.left = helper()
            node.right = helper()

            return node
        ans = helper()
        return ans
