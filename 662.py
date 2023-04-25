# 662. Maximum Width of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        st = deque([(root, 0)])
        res = 0
        while st:
            n = len(st)
            parent = st[0][1]
            
            for i in range(n):
                cur, idx = st.popleft()
                
                if cur.left:
                    st.append((cur.left, idx * 2 + 1))
                if cur.right:
                    st.append((cur.right, idx * 2 + 2))
            
            res = max(res, idx - parent + 1)
        
        return res
                
                