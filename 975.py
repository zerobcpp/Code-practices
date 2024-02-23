# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        
        def helper(node):
            if not node:
                return
            
            if low <= node.val <= high:
                self.res += node.val
            for child in [node.left, node.right]:
                helper(child)
        
        helper(root)
        return self.res
    
    
    def rangeSumBST(self, root, low, high):
        st = [root]
        res = 0
        while st:
            cur = st.pop()
            if not cur:
                continue
            if low <= cur.val <= high:
                res += cur.val
            
            for child in [cur.left, cur.right]:
                st.append(child)
        
        return res
    
    
    def rangeSumBSTMorris(self, root, l, h):
        res = 0
        
        while root:
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                
                temp.right = root
                temp = root.left
                root.left = None
                root = temp
            else:
                if l <= root.val <= h:
                    res += root.val
                root = root.right
        
        return res