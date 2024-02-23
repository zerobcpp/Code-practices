# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        st = [(root, float(inf), -float(inf))]
        seen = set()
        while st:
            cur, high, low = st.pop()
            if cur.val < low or cur.val > high or cur.val in seen:
                return False
            seen.add(cur.val)
            if cur.left:
                st.append((cur.left, cur.val, low))
            if cur.right:
                st.append((cur.right, high, cur.val))
        
        return True
            