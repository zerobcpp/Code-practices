# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(node, sm):
            if not node:
                return
            if not node.left and not node.right and sm-node.val == 0:
                return True
            
            return helper(node.left, sm-node.val) or helper(node.right, sm - node.val)
        
        return helper(root, targetSum)