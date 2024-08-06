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
    
    def diameterOfBinaryTree(self, root):
        left = float('inf')
        right = -float('inf')
        
        st = [(root, 0)]
        
        while st:
            cur, length = st.pop()
            left = min(length, left)
            right = max(length, right)
            
            if cur.left:
                st.append((cur.left, length - 1))
            if cur.right:
                st.append((cur.right, length + 1))
        
        #print(left, right)
        
        return -left + right