# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        prev = None
        cnt = 0
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            cnt += 1
        if cnt == 0:
            return None
        prev.next = slow.next
        #print(slow)
        return head