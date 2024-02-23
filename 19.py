# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(-999)
        dummyNode.next = head
        fast = slow = dummyNode.next 
        for _ in range(n):
            fast = fast.next
        if not fast:
            return dummyNode.next.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        #
        slow.next = slow.next.next
        
        return dummyNode.next