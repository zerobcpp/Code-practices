# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        c = []
        
        def helper(node):
            if not node:
                return
            helper(node.left)
            c.append(node.val)
            helper(node.right)
        
        helper(root)
        
        dummy = cur = TreeNode(-1)
        N = len(c)
        for i in range(N):
            val = c[i]
            cur.right = TreeNode(val)
            cur.left = None
            cur = cur.right
        
        return dummy.right
    
    
    def increasingBST(self, root): 
        if not root:
            return 
        dummy = prev = TreeNode(-1)
        
        while root:
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right

                temp.right = root
                left = root.left
                root.left = None
                root = left
            else:
                prev.right = root
                prev = prev.right
                root = root.right
        
        #print(dummy)
        return dummy.right