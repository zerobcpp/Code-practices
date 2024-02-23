# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        st = [(root, None)]
        c = defaultdict(list)
        while st:
            cur, parent = st.pop()
            if parent:
                c[parent.val].append(cur.val)
                c[cur.val].append(parent.val)
            for child in [cur.left, cur.right]:
                if child:
                    st.append((child, cur))
        #print(c)
        st = [(target.val, k)]
        seen = set([target.val])
        res = []
        while st:
            cur, level = st.pop()
            #print(c[cur])
            if level == 0:
                res.append(cur)
            for neigh in c[cur]:
                if neigh not in seen:
                    seen.add(neigh)
                    st.append((neigh, level - 1))

        return res
            