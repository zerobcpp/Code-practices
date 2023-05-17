# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        cur = head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        i = 0
        while cur.next and cur.next.next:
            one = cur.next
            two = cur.next.next
            cur.next = two
            
            
            one.next = two.next
            two.next = one
            
            cur = cur.next.next
        return dummy.next