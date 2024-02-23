# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c = defaultdict(int)
        def helper(node):
            if not node:
                return
            c[node.val] += 1
            for child in [node.left, node.right]:
                if child:
                    helper(child)
            
        helper(root)
        f = max(c.values())
        res = []
        
        for i, v in c.items():
            if v == f:
                res.append(i)
        
        print()
        return res