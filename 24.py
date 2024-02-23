# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        cur = head
        count = 0
        while cur:
            if not count & 1 and cur.next:
                cur.val, cur.next.val = cur.next.val, cur.val
            
            count += 1
            cur = cur.next
        
        return head