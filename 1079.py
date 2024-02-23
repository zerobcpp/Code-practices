# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def helper(node, cur):
            nonlocal ret
            if not node:
                ret += int(cur, 2)
                return
            for child in [node.left, node.right]:
                helper(child, cur + str(node.val))
                    
        helper(root, '')
        return ret//2
            