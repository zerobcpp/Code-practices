# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        
        st = [(root, 1)]
        
        while st:
            cur, dep = st.pop()
            
            if dep == depth-1:
                temp = TreeNode(val)
                temp.left = cur.left
                cur.left = temp
                temp = TreeNode(val)
                temp.right = cur.right
                cur.right = temp
            
            
            if cur.left:
                st.append((cur.left, dep + 1))
            if cur.right:
                st.append((cur.right, dep + 1))

        
        return root