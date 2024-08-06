# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
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
        while cur:
            if cur.next and cur.val > cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        
        return helper(head)
        