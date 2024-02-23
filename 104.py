# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
    
    def maxDepth(self, root):
        
        def helper(node):
            if not node:
                return 0
            left = helper(node.left) + 1
            right = helper(node.right) + 1
            return max(left, right)
        
        return helper(root)
    
    def maxDepth(self, root):
        if not root:
            return 0
        st = [(root, 0)]
        res = 0
        while st:
            cur, level = st.pop()
            res = max(res, level)
            
            for child in [cur.left, cur.right]:
                if child:
                    st.append((child, level + 1))
        
        return res + 1