# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        x = head
        count = 0
        while x:
            nodes.append(x)
            x = x.next
            count += 1
        
        n = len(nodes)
        

        return nodes[n//2]