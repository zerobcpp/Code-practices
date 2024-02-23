# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        val = []
        while cur:
            val.append(cur.val)
            cur = cur.next
        
        l, r = 0, len(val) - 1
        res = 0
        while l < r:
            res = max(res, val[l] + val[r])
            l += 1
            r -= 1
        
        return res