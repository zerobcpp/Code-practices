# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = set()
        cur = head
        while cur:
            t.add(cur.val)
            cur = cur.next
        
        dummy = ListNode(-1)
        cur = dummy
        while t:
            val = t.pop()
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        
        return dummy.next
        
        