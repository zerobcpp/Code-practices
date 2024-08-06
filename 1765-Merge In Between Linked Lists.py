# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        res = []
        cur = list1
        i = 0
        
        while cur and i < b:
            if not (i >= a and i < b):
                res.append(cur.val)
            cur = cur.next
            i += 1
        cur = cur.next   
        bcur = list2
        while bcur:
            res.append(bcur.val)
            bcur = bcur.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        dummy = cur = ListNode(-1)
        
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
        
        return dummy.next
    
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode):
        slow = fast = list1
        while b:
            fast = fast.next
            b -= 1
        
        prev = None
        while a:
            prev = slow
            slow = slow.next
            a -= 1
        
        cur = list2
        while cur.next:
            cur = cur.next
        cur.next = fast.next
        prev.next = list2
        #print(slow.val, fast.val)
        
        return list1
        