"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        st = [head]
        prev = Node(None, None, None, None)
        
        while st:
            cur = st.pop()
            if cur.next:
                st.append(cur.next)
            if cur.child:
                st.append(cur.child)
                cur.child = None
            prev.next = cur
            cur.prev = prev
            prev = cur
        
        #self.dbg(head)
        head.prev = None
        return head
    
    
    def dbg(self, node):
        cur = node
        while cur.next:
            print(cur.val, cur.next.val, '->')
            cur = cur.next
        