# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = 10 ** 5 + 1
        prev = None
        def helper(node):
            nonlocal res, prev
            if not node:
                return
            helper(node.left)
            if prev:
                res = min(res, abs(node.val - prev.val))
            prev = node
            helper(node.right)
            
        helper(root)
        return res
    
    def getMinimumDifference(self, root):
        res = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        
        helper(root)
        ret = 10 ** 5
        for i in range(1, len(res)):
            ret = min(ret, res[i] - res[i-1])
        
        return ret
            
            
            