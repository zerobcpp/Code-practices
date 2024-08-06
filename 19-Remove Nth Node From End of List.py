# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        dummy = ListNode(-1)
        dummy.next = head
        
        for _ in range(n):
            fast = fast.next
        slow = head
        while fast and fast.next:
            #prev = slow
            slow = slow.next
            fast = fast.next
        
        if not fast:
            return dummy.next.next
        slow.next = slow.next.next
        return dummy.next