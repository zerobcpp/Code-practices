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
            
        
        
    def addTwoNumbers(self, l1, l2):
        def reverse(node):
            prev = None
            x = node
            while x:
                y = x.next
                x.next = prev
                prev = x
                x = y
            
            return prev
        l1 = reverse(l1)
        l2 = reverse(l2)
        head = None
        carry = digit = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            digit = (carry + v1 + v2) % 10
            carry = (carry + v1 + v2) // 10
            
            cur = ListNode(digit)
            cur.next = head
            head = cur
            #print(head)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else 0
        
        if carry:
            cur = ListNode(carry)
            cur.next = head
            head = cur
        
        return head
            
            