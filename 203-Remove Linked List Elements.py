# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)
        prev.next = head
        cur = head
        while cur:
            if cur.val != val:
                prev = cur
            else:
                prev.next = cur.next
            
            cur = cur.next
        
        return dummy.next
            