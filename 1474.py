# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def helper(node, path, cnt):
            nonlocal res
            if not node:
                return
            res = max(cnt, res)
            if path:
                helper(node.left, not path, cnt + 1)
                helper(node.left, path, 0)
            else:
                helper(node.right, not path, cnt + 1)
                helper(node.right, path, 0)
        
        helper(root, True, 0)
        helper(root, False, 0)
        return res