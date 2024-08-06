# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(10000)
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        res = res
        sm = 0
        for i in res:
            sm = sm * 10 + i
            
        sm *= 2
        cur = dummy = ListNode(-1)
        for i in str(sm):
            n = ListNode(int(i))
            cur.next = n
            cur = cur.next
        
        return dummy.next
            
    
    def doubleIt(self, head):
        res = []
        def helper(node):
            if not node:
                return
            prev = None
            x = node
            while x:
                y = x.next
                x.next = prev
                prev = x
                x = y
            return prev
        
        head = helper(head)
        cur = head
        dummy = prev = ListNode(-1)
        carry = digit = 0
        while cur:
            
            val = cur.val * 2 if cur else 0
            
            digit = (carry + val) % 10
            carry = (carry + val) // 10
            
            n = ListNode(digit)
            prev.next = n
            prev = prev.next
            cur = cur.next
        
        if carry > 0:
            prev.next = ListNode(carry)
        return helper(dummy.next)
            
            
            
            