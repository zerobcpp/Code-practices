# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []
        def helper(n1):
            if not n1:
                return
            if not n1.left and not n1.right:
                r1.append(n1.val)
            helper(n1.left)
            helper(n1.right)
        
        def helper2(n2):
            if not n2:
                return
            if not n2.left and not n2.right:
                r2.append(n2.val)
            helper2(n2.left)
            helper2(n2.right)
        
        helper(root1)
        helper2(root2)
        
        
        return r1 == r2
    
    
    def leafSimiliar(self, r1, r2):
        l1 = []
        l2 = []
        def helper(node, arr):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)
            helper(node.left)
            helper(node.right)
        
        helper(r1, l1)
        helper(r2, l2)
        return l1 == l2