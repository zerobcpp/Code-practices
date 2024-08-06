# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        resleft = []
        resright = []
        
        def left(root):
            if not root:
                resleft.append(None)
                return
            resleft.append(root.val)
            left(root.left)
            left(root.right)
        
        def right(root):
            if not root:
                resright.append(None)
                return
            resright.append(root.val)
            right(root.right)
            right(root.left)
        
        left(root.left)
        right(root.right)
        print(resleft,resright)
        return resleft == resright