# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        dummy = start = ListNode(-1)
        while cur:
            fast = None
            if cur.val == 0 and cur.next:
                sm = 0
                fast = cur.next
                while fast and fast.val != 0:
                    sm += fast.val
                    fast = fast.next
                
                start.next = ListNode(sm)
                start = start.next
                    
                    
            cur = cur.next if not fast else fast
        
        return dummy.next