# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
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
    
    def minDepth(self, root):
        self.res = float('inf')
        def helper(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.res = min(self.res, depth)
            helper(node.left, depth + 1), helper(node.right, depth + 1)
        helper(root, 1)
        return self.res if self.res != float('inf') else 0
            