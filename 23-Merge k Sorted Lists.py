# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for node in lists:
            while node:
                heappush(l, node.val)
                node = node.next
        
        head = cur = ListNode(-1)
        while l:
            v = (heappop(l))
            cur.next = ListNode(v)
            cur = cur.next
        
        return head.next
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for node in lists:
            while node:
                l.append(node .val)
                node = node.next
        
        l.sort()
        dummy = cur = ListNode(-1)
        n = len(l)
        for i in range(n):
            v = ListNode(l[i])
            cur.next = v
            cur = cur.next
        
        return dummy.next