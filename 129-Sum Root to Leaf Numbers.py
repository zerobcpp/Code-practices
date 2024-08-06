# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        st = [(root, 0)]
        
        while st:
            cur, val = st.pop()
            val += cur.val
            
            if not cur.left and not cur.right:
                res.append(val)
            
            for child in [cur.left, cur.right]:
                if child:
                    st.append((child, val*10))

        return sum(res)
            
        