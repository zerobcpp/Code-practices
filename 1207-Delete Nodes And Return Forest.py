# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        
        def helper(node, route = []):
            if not node:
                return None
            
            node.left = helper(node.left)
            node.right = helper(node.right)
            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                
                return None
            
            return node
        
        root = helper(root, res)
        #print(root)
        #print(res)
        if root:
            res.append(root)
        return res
    
    
    def delNodes(self, root, delete):
        delete = set(delete)
        st = deque([root])
        res = []
        while st:
            cur = st.popleft()
            if not cur:
                continue

            if cur.left:
                st.append(cur.left)
                if cur.left.val in delete:
                    cur.left = None
            if cur.right:
                st.append(cur.right)
                if cur.right.val in delete:
                    cur.right = None
            
            if cur.val in delete:
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
        
        if root.val not in delete:
            res.append(root)
        
        return res
                