# 1721. Swapping Nodes in a Linked List

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
            
    
    def swapNodes(self, head, k):
        
        swap = head
        for i in range(k-1):
            swap = swap.next
            
        nextswap = head
        end = swap
        while end.next:
            nextswap = nextswap.next
            end = end.next
        
        swap.val, nextswap.val = nextswap.val, swap.val
        
        return head
        
        
        