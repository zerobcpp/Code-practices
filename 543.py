# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def countL(root):
            if not root:
                return 0
            else:
                return 1 + countL(root.left)
        
        def countR(root):
            if not root:
                return 0
            else:
                return 1 + countR(root.right)
        l = countL(root.left)
        r = countR(root.right)
        
        return l + r