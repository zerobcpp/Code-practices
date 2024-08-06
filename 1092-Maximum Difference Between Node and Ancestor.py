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
    
    
    
    def maxAncestorDiff(self, root):
        st = [(root, 0, 10 ** 5)]
        res = 0
        while st:
            cur, cmx, cmn = st.pop()
            mx = max(cur.val, cmx)
            mn = min(cur.val, cmn)
            res = max(res, mx - mn)
            
            for child in [cur.left, cur.right]:
                if child:
                    st.append((child, mx, mn))
        
        return res
            