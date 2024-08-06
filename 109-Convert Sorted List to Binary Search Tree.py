# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        def helper(l, r):
            if l > r:
                return None
            mid = l + (r - l) // 2
            
            left = helper(l, mid-1)
            right = helper(mid+1, r)
            n = TreeNode(res[mid], left, right)
            return n
        
        return helper(0, len(res)-1)