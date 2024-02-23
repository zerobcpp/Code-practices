# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = []
        cur = head
        while cur:
            node.append(cur.val)
            cur = cur.next
        
        dummy = ListNode(-1)
        cur = dummy
        n = len(node)
        node[k-1], node[n-k] = node[n-k], node[k-1]
        
        for i in range(n):
            newNode = ListNode(node[i])
            cur.next = newNode
            cur = cur.next
        
        return dummy.next
            
            