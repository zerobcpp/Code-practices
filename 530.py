# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = 10 ** 5 + 1
        
        def helper(node):
            nonlocal res
            if node.left:
                res = min(res, abs(node.val - node.left.val))
                helper(node.left)
            if node.right:
                res = min(res, abs(node.val - node.right.val))
                helper(node.right)
        helper(root)
        return res