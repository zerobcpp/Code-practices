# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(-1, head)
        prev = dummy
        for i in range(left-1):
            prev = prev.next
        
        cur = prev.next
        #print(cur.val)
        
        for _ in range(right - left):
            nn = cur.next
            cur.next = nn.next
            nn.next = prev.next
            prev.next = nn
            
            #print()
            
            #self.debug(head)
        
        return dummy.next
    
    
    def debug(self, node):
        x = node
        while x:
            print(x.val, end = ' ->')
            x = x.next
        
        print()
        