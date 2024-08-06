# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        cur = head
        while cur:
            res.append(cur)
            cur = cur.next
        
        n =len(res)
        return res[n//2]
    
    
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow