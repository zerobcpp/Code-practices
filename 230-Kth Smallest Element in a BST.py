# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        arr = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            arr.append(root.val)
            helper(root.right)
            
        helper(root)
        arr.sort()
        return arr[k-1]