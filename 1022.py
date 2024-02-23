# 1022. Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def helper(node, cur):
            if not node:
                return
            nonlocal ret
            for child in [node.left, node.right]:
                helper(child, cur + str(node.val))
                
            if not node.left and not node.right:
                cur += str(node.val)
                ret += int(cur, 2)
                
            
                    
        helper(root, '')
        return ret
    
    def sumRootToLeaf(self, root):
        ret = 0
        def helper(node, cur):
            if not node.left and not node.right:
                nonlocal ret
                ret += 2 * cur + node.val
            
            for child in [node.left, node.right]:
                if child:
                    helper(child, 2 * cur + node.val)
        
        helper(root, 0)
        return ret
            
        
