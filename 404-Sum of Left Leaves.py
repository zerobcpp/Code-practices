# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(node, left):
            if not node:
                return
            if not node.left and not node.right and left:
                self.res += node.val
            
            helper(node.left, True)
            helper(node.right, False)
        
        helper(root, False)
        return self.res
    
    def sumofLeftLeaves(self, root):
        st = [(root, False)]
        res = 0
        while st:
            cur, left = st.pop()
            
            if left and cur.left == None and cur.right == None:
                res += cur.val
            if not cur:
                continue
            st.append((cur.left, True))
            st.append((cur.right, False))
        
        return res
            
                