# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            x = stack.pop()
            if x:
                stack.append(x.left)
                stack.append(x.right)
                x.left, x.right = x.right, x.left 
        return root
    
    
    def invertTree(self, root):
        def helper(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            helper(node.left)
            helper(node.right)
        helper(root)
        return root