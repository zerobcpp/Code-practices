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
        
        t = sorted(t, reverse = True)
        dummy = ListNode(-1)
        cur = dummy
        while t:
            val = t.pop()
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        
        return dummy.next
    
    def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head