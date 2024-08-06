# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        c = defaultdict(list)
        st = deque([root])
        level = 0
        while st:
            n = len(st)
            
            for i in range(n):
                cur = st.popleft()
                c[level].append(cur.val)
                
                for child in [cur.left, cur.right]:
                    if child:
                        st.append(child)
            
            level += 1
        
        #print(level, c)
        return c[level-1][0]
    
    def findBottomLeftValue(self, root):
        st = deque([root])
        
        while st:
            n = len(st)
            for i in range(n):
                cur = st.popleft()
                
                for child in [cur.right, cur.left]:
                    if child:
                        st.append(child)
        
        
        return cur.val