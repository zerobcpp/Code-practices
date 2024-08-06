# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        op = []
        val = []
        def helper(node):
            if not node:
                return
            if node.val in [2, 3]:
                op.append(node.val)
            else:
                if node.val == 1:
                    val.append(True)
                else:
                    val.append(False)
        
            helper(node.left)
            helper(node.right)
        
        helper(root)
        #print(val, op)
        res = None
        while op:
            p = val.pop()
            q = val.pop()
            o = op.pop()
            
            if o == 2:
                res = p or q
            else:
                res = p and q
            
            val.append(res)
        
        return res if res else False
    
    
    def evaluateTree(self, root):
        
        def helper(node):
            if not node.left and not node.right:
                return node.val == 1
            
            left = helper(node.left)
            right = helper(node.right)
            res = None
            if node.val == 2:
                res = left | right
            else:
                res = left & right
            
            return res
        
        return helper(root)
                