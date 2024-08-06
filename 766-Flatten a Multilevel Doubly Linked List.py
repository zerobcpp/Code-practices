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
        if not head:
            return None
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
    
    
    def flatten(self, head):
        if not head:
            return None
        cur = head
        while cur:
            if cur.child:
                child = cur.child
                while child.next:
                    child = child.next
                child.next = cur.next
                if cur.next:
                    cur.next.prev = child
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            cur = cur.next
        
        self.debug(head)
        return head
        
    def debug(self, node):
        while node.next:
            print(node.prev,node,node.next, node.val, node.child)
            node = node.next
                
        