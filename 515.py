# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = deque([root])
        
        while st:
            n = len(st)
            temp = []
            for i in range(n):
                cur = st.popleft()
                temp.append(cur.val)
                
                for child in [cur.left, cur.right]:
                    if child:
                        st.append(child)
            
            res.append(max(temp))
        
        return res