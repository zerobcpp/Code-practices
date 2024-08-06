# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        st = [(root, [])]
        res = []
        while st:
            cur, s = st.pop()
            if not cur:
                continue
            s.append(str(cur.val))
            if not cur.left and not cur.right:
                sol = []
                for i in s:
                    sol.append(chr(int(i) + ord('a')))
                res.append(sol[::-1])
            for child in [cur.left, cur.right]:
                if child:
                    st.append((child, s[:]))
        
        res.sort()
        #print(res)
        
        return ''.join(res[0])
    
    
    def smallestFromLeaf(self, root):
        st = [(root, [])]
        res = '~'
        
        while st:
            cur, s = st.pop()
            
            s.append(chr(ord('a') + cur.val))
            if not cur.left and not cur.right:
                res = min(res, ''.join(s[::-1]))
            
            for child in [cur.left, cur.right]:
                if child:
                    st.append((child, s[:]))
        
        return res