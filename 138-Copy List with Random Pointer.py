"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        c = {}
        while cur:
            c[cur] = Node(cur.val)
            cur = cur.next
            
        cur = head
        start = dummy = Node(-1)
        
        
        while cur:
            n = c[cur]
            r_node = c.get(cur.random, None)
            
            n.random = r_node
            #print(r_node)
            start.next = n
            start = start.next
            cur = cur.next
        
        return dummy.next
            
