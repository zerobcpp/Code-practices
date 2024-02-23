# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, mx, mn):
            if not node:
                return mx - mn
            mx = max(node.val, mx)
            mn = min(node.val, mn)
            return max(helper(node.left, mx, mn), helper(node.right, mx, mn))
        
        return helper(root, 0, 10 ** 5)