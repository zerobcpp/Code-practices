# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf = []
        st = [root]
        parent = {}
        while st:
            cur = st.pop()
            if not cur.left and not cur.right:
                leaf.append(cur)
            for neigh in [cur.left, cur.right]:
                if neigh:
                    st.append(neigh)
                    parent[neigh] = cur
        res = 0
        print(leaf)
        while leaf:
            cur = leaf.pop()
            st = [(cur, 0)]
            
            seen = set([cur])
            
            while st:
                cur, cnt = st.pop()
                if not cur.left and not cur.right and cnt <= distance:
                    if cnt != 0:
                        res += 1
                if cnt > distance:
                    continue
                for neigh in [cur.left, cur.right, parent.get(cur, None)]:
                    if neigh and neigh not in seen:
                        seen.add(neigh)
                        st.append([neigh, cnt + 1])
                
                #print(st)
                
                
        #print(res)
        return res // 2
            
