# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTitr(self, root: Optional[TreeNode]) -> bool:
        st = [(root, float(inf), -float(inf))]
        #seen = set()
        while st:
            cur, high, low = st.pop()
            if cur.val <= low or cur.val >= high:
                return False
            if cur.left:
                st.append((cur.left, cur.val, low))
            if cur.right:
                st.append((cur.right, high, cur.val))
        
        return True

    
    def isValidBST(self, root):
        def helper(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            
            return helper(node.left, low, node.val) \
            and helper(node.right, node.val, high)
        
        return helper(root, -float('inf'), float('inf'))
            