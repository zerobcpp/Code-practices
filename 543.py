# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.count = 0
        def helper(root):
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            self.count = max(l+r,self.count)
            return 1 + max(l, r)
        
        helper(root)
        return self.count