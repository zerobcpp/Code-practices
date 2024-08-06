# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l, r):
            if l > r:
                return None
            mid = l + (r - l) // 2
            n = TreeNode(nums[mid])
            left = helper(l, mid-1)
            right = helper(mid+1, r)
            n.left, n.right = left, right
            return n
        
        return helper(0, len(nums)-1)