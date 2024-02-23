# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        st = [(root, 1)]
        res = float('inf')
        while st:
            cur, depth = st.pop()
            
            if not cur.left and not cur.right:
                res = min(res, depth)
            if cur.left:
                st.append((cur.left, depth + 1))
            if cur.right:
                st.append((cur.right, depth + 1))
        
        return res
            