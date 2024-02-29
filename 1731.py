# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        c = defaultdict(list)
        st = deque([root])
        p = 0
        while st:
            n = len(st)
            p = 1 - p
            
            for i in range(n):
                cur = st.popleft()
                if p:
                    if cur.val & 1 == 0 or (len(c[level]) >= 1 and c[level][-1] >= cur.val):
                        return False
                else:
                    if cur.val & 1 == 1 or (len(c[level]) >= 1 and c[level][-1] <= cur.val):
                        return False
                c[level].append(cur.val)
                for child in [cur.left, cur.right]:
                    if child:
                        st.append(child)
                
            #print(c)
            level += 1
        
        return True
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        st = deque([root])
        p = 0
        while st:
            n = len(st)
            p = 1 - p
            mx = None
            for i in range(n):
                cur = st.popleft()
                if p:
                    if cur.val & 1 == 0 or (mx != None and mx >= cur.val):
                        return False
                else:
                    if cur.val & 1 == 1 or (mx != None and mx <= cur.val):
                        return False
                mx = cur.val
                for child in [cur.left, cur.right]:
                    if child:
                        st.append(child)
                
            #print(c)
            level += 1
        
        return True