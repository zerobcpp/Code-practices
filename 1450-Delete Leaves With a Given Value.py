# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def helper(node):
            if not node:
                return
            
            node.left = helper(node.left)
            node.right = helper(node.right)
            if node.val == target and not node.left and not node.right:
                return None
            
            return node
        
        return helper(root)