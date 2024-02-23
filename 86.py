# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s = []
        t = []
        
        cur = head
        
        while cur:
            if cur.val < x: 
                s.append(cur.val)
            else:
                t.append(cur.val)
            cur = cur.next
        
        dummy = start = ListNode(-1)
        
        for i in range(len(s)):
            start.next = ListNode(s[i])
            start = start.next
        
        for i in range(len(t)):
            start.next = ListNode(t[i])
            start = start.next
        
        return dummy.next