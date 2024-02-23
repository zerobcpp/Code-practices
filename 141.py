# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
    
    def hasCycle(self, head):
        cycle = set()
        cur = head
        
        while cur:
            if cur in cycle:
                #print(cur.val)
                return True
            
            cycle.add(cur)
            cur = cur.next
        
        return False