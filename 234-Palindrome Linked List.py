# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        copy = []
        x = head
        while x:
            copy.append(x.val)
            x = x.next
        
        return copy == copy[::-1]
    
    def isPalindrome(self, head):
        slow = fast = head
        
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            x = slow.next
            slow.next = prev
            prev = slow
            slow = x
            
        if fast:
            slow = slow.next
        #print(prev.val, slow.val)
        
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        
        return True
            