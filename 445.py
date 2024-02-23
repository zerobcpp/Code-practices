# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        while l1:
            s1.append(str(l1.val))
            l1 = l1.next
        
        s2 = []
        while l2:
            s2.append(str(l2.val))
            l2 = l2.next
        
        x = int(''.join(s1)) + int(''.join(s2))
        
        cur = dummy = ListNode(-1)
        for i in str(x):
            cur.next = ListNode(i)
            cur = cur.next
        
        return dummy.next
            
        
        