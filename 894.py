# 894. All Possible Full Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}
        def helper(left):
            if left % 2 == 0:
                return None
            if left == 1:
                return [TreeNode(0)]
            
            count = []
            for i in range(1, left, 2):
                l = helper(i)
                r = helper(left - i - 1)
                
                for nl in l:
                    for nr in r:
                        cur = TreeNode(0, nl, nr)
                        count.append(cur)
            cache[left] = count
            return count
        helper(n)
        return cache[n]