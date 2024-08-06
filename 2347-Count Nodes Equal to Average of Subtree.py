# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(node):
            sm, cnt = node.val, 1
            for child in [node.left, node.right]:
                if child:
                    s, c = helper(child)
                    sm += s
                    cnt += c
            #print(node.val, sm, cnt)
            if node.val == sm // cnt:
                #print(node.val, sm, cnt)
                self.res += 1
            
            return [sm, cnt]
                    
        helper(root)
        return self.res