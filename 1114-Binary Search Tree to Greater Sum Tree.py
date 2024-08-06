# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cur = 0
        def helper(node):
            if not node:
                return 0
            
            helper(node.right)
            self.cur += node.val
            node.val = self.cur
            helper(node.left)
        
        helper(root)
        return root
            