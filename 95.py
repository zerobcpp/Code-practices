# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        res = []
        cache = {}
        def helper(l, r):
            
            if l > r:
                return [None]
            elif l == r:
                cache[l, r] = [TreeNode(l)]
                return cache[l, r]
            if (l, r) in cache:
                return cache[l, r]
            count = []
            for i in range(l, r + 1):
                left = helper(l, i-1)
                right = helper(i+1, r)
                #print(left)
                for ln in left:
                    for rn in right:
                        cur = TreeNode(i, ln, rn)
                        count.append(cur)
            cache[l,r] = count
            return count
        
        return helper(1, n)
            