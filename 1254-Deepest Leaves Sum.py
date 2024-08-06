# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        st = [(root, 0)]
        c = defaultdict(list)
        l = 0
        while st:
            cur, level = st.pop()
            c[level].append(cur.val)
            l = max(l, level)
            for child in [cur.left, cur.right]:
                if child:
                    st.append((child, level + 1))
        
        #print(c)
        return sum(c[l])