    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, description: List[List[int]]) -> Optional[TreeNode]:
        c = {}
        adj = defaultdict(int)
        for p, child, left in description:
            if p not in c:
                c[p] = [None, None]
            if left == 1:
                c[p][1] = child
            else:
                c[p][0] = child
            
            adj[child] += 1
        
        st = []
        for i, v in c.items():
            if adj[i] == 0:
                root = TreeNode(i)
                st.append(root)
                break
        
        dummy = TreeNode(-1, root, None)
        while st:
            cur = st.pop()
            val = cur.val
            
            if val in c:
                right, left = c[val]
                if left:
                    cur.left = TreeNode(left)
                    st.append(cur.left)
                if right:
                    cur.right = TreeNode(right)
                    st.append(cur.right)
        
        return dummy.left