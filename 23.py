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