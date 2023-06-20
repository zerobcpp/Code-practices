# 530. Minimum Absolute Difference in BST

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = 10 ** 5 + 1
        prev = None
        def helper(node):
            nonlocal res, prev
            if not node:
                return
            helper(node.left)
            if prev:
                res = min(res, abs(node.val - prev.val))
            prev = node
            helper(node.right)
            
        helper(root)
        return res