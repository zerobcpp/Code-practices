# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def helper(node):
            if not node:
                return
            res.append(str(node.val))
            if node.left or node.right:
                res.append('(')
                helper(node.left)
                res.append(')')
            if node.right:
                res.append('(')
                helper(node.right)
                res.append(')')
            
        
        helper(root)
        #print(res)
        return ''.join(res)